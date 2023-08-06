from __future__ import annotations

import logging
from collections.abc import Sequence
from dataclasses import dataclass
from types import TracebackType
from typing import Any

import aiohttp
from aiohttp import ClientResponseError
from yarl import URL

from .entities import (
    BucketsConfig,
    CloudProviderType,
    Cluster,
    CredentialsConfig,
    DisksConfig,
    DNSConfig,
    IngressConfig,
    MetricsConfig,
    MonitoringConfig,
    NodePool,
    NodePoolTemplate,
    NotificationType,
    OrchestratorConfig,
    RegistryConfig,
    ResourcePreset,
    SecretsConfig,
    StorageConfig,
)
from .factories import EntityFactory, PayloadFactory

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class _Endpoints:
    clusters: URL
    cloud_providers: URL

    def cluster(self, cluster_name: str) -> URL:
        return self.clusters / cluster_name

    def node_pools(self, cluster_name: str) -> URL:
        return self.cluster(cluster_name) / "cloud_provider/node_pools"

    def node_pool(self, cluster_name: str, node_pool_name: str) -> URL:
        return self.node_pools(cluster_name) / node_pool_name

    def storages(self, cluster_name: str) -> URL:
        return self.cluster(cluster_name) / "cloud_provider/storages"

    def storage(self, cluster_name: str, storage_name: str) -> URL:
        return self.storages(cluster_name) / storage_name

    def notifications(self, cluster_name: str) -> URL:
        return self.cluster(cluster_name) / "notifications"

    def resource_presets(self, cluster_name: str) -> URL:
        return self.cluster(cluster_name) / "orchestrator/resource_presets"

    def resource_preset(self, cluster_name: str, preset_name: str) -> URL:
        return self.resource_presets(cluster_name) / preset_name

    @classmethod
    def create(cls, base_url: URL) -> _Endpoints:
        clusters = base_url / "api/v1/clusters"
        return cls(
            clusters=clusters,
            cloud_providers=base_url / "api/v1/cloud_providers",
        )


class ConfigClient:
    def __init__(
        self,
        url: URL,
        token: str | None = None,
        timeout: aiohttp.ClientTimeout = aiohttp.client.DEFAULT_TIMEOUT,
        trace_configs: Sequence[aiohttp.TraceConfig] = (),
    ):
        self._endpoints = _Endpoints.create(url)
        self._token = token
        self._timeout = timeout
        self._trace_configs = trace_configs
        self._client: aiohttp.ClientSession | None = None
        self._entity_factory = EntityFactory()
        self._payload_factory = PayloadFactory()

    async def __aenter__(self) -> "ConfigClient":
        self._client = await self._create_http_client()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        assert self._client
        await self._client.close()

    async def _create_http_client(self) -> aiohttp.ClientSession:
        client = aiohttp.ClientSession(
            timeout=self._timeout,
            trace_configs=list(self._trace_configs),
        )
        return await client.__aenter__()

    def _create_headers(self, *, token: str | None = None) -> dict[str, str]:
        result = {}
        token = token or self._token
        if token:
            result["Authorization"] = f"Bearer {token}"
        return result

    async def get_clusters(self, *, token: str | None = None) -> Sequence[Cluster]:
        assert self._client
        headers = self._create_headers(token=token)
        async with self._client.get(
            self._endpoints.clusters, headers=headers
        ) as response:
            response.raise_for_status()
            payload = await response.json()
            return [self._entity_factory.create_cluster(p) for p in payload]

    async def get_cluster(self, name: str, *, token: str | None = None) -> Cluster:
        assert self._client
        headers = self._create_headers(token=token)
        async with self._client.get(
            self._endpoints.cluster(name), headers=headers
        ) as response:
            response.raise_for_status()
            payload = await response.json()
            return self._entity_factory.create_cluster(payload)

    async def create_blank_cluster(
        self,
        name: str,
        service_token: str,
        *,
        token: str | None = None,
        ignore_existing: bool = False,
    ) -> Cluster:
        assert self._client
        headers = self._create_headers(token=token)
        payload = {"name": name, "token": service_token}
        try:
            async with self._client.post(
                self._endpoints.clusters, headers=headers, json=payload
            ) as resp:
                resp.raise_for_status()
                resp_payload = await resp.json()
                return self._entity_factory.create_cluster(resp_payload)
        except ClientResponseError as e:
            is_existing = e.status == 400 and "already exists" in e.message
            if not ignore_existing or is_existing:
                raise
        return await self.get_cluster(name)

    async def patch_cluster(
        self,
        name: str,
        *,
        token: str | None = None,
        credentials: CredentialsConfig | None = None,
        storage: StorageConfig | None = None,
        registry: RegistryConfig | None = None,
        orchestrator: OrchestratorConfig | None = None,
        monitoring: MonitoringConfig | None = None,
        secrets: SecretsConfig | None = None,
        metrics: MetricsConfig | None = None,
        disks: DisksConfig | None = None,
        buckets: BucketsConfig | None = None,
        ingress: IngressConfig | None = None,
        dns: DNSConfig | None = None,
    ) -> Cluster:
        assert self._client
        url = self._endpoints.cluster(name)
        headers = self._create_headers(token=token)
        payload: dict[str, Any] = {}
        if credentials:
            payload["credentials"] = self._payload_factory.create_credentials(
                credentials
            )
        if storage:
            payload["storage"] = self._payload_factory.create_storage(storage)
        if registry:
            payload["registry"] = self._payload_factory.create_registry(registry)
        if orchestrator:
            payload["orchestrator"] = self._payload_factory.create_orchestrator(
                orchestrator
            )
        if monitoring:
            payload["monitoring"] = self._payload_factory.create_monitoring(monitoring)
        if secrets:
            payload["secrets"] = self._payload_factory.create_secrets(secrets)
        if metrics:
            payload["metrics"] = self._payload_factory.create_metrics(metrics)
        if disks:
            payload["disks"] = self._payload_factory.create_disks(disks)
        if buckets:
            payload["buckets"] = self._payload_factory.create_buckets(buckets)
        if ingress:
            payload["ingress"] = self._payload_factory.create_ingress(ingress)
        if dns:
            payload["dns"] = self._payload_factory.create_dns(dns)
        async with self._client.patch(url, headers=headers, json=payload) as resp:
            resp.raise_for_status()
            resp_payload = await resp.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def delete_cluster(self, name: str, *, token: str | None = None) -> None:
        assert self._client
        headers = self._create_headers(token=token)
        async with self._client.delete(
            self._endpoints.cluster(name), headers=headers
        ) as resp:
            resp.raise_for_status()

    async def add_storage(
        self,
        cluster_name: str,
        storage_name: str,
        size: int | None = None,
        *,
        token: str | None = None,
        start_deployment: bool = True,
        ignore_existing: bool = False,
    ) -> Cluster:
        assert self._client
        try:
            url = self._endpoints.storages(cluster_name)
            headers = self._create_headers(token=token)
            payload: dict[str, Any] = {"name": storage_name}
            if size is not None:
                payload["size"] = size
            async with self._client.post(
                url.with_query(start_deployment=str(start_deployment).lower()),
                headers=headers,
                json=payload,
            ) as response:
                response.raise_for_status()
                resp_payload = await response.json()
                return self._entity_factory.create_cluster(resp_payload)
        except ClientResponseError as e:
            if not ignore_existing or e.status != 409:
                raise
        return await self.get_cluster(cluster_name)

    async def patch_storage(
        self,
        cluster_name: str,
        storage_name: str | None,
        ready: bool | None = None,
        *,
        token: str | None = None,
        ignore_not_found: bool = False,
    ) -> Cluster:
        assert self._client
        try:
            if storage_name:
                url = self._endpoints.storage(cluster_name, storage_name)
            else:
                url = self._endpoints.storage(cluster_name, "default/entry")
            headers = self._create_headers(token=token)
            payload: dict[str, Any] = {}
            if ready is not None:
                payload["ready"] = ready
            async with self._client.patch(
                url, headers=headers, json=payload
            ) as response:
                response.raise_for_status()
                resp_payload = await response.json()
                return self._entity_factory.create_cluster(resp_payload)
        except ClientResponseError as e:
            if not ignore_not_found or e.status != 404:
                raise
        return await self.get_cluster(cluster_name)

    async def remove_storage(
        self,
        cluster_name: str,
        storage_name: str,
        *,
        token: str | None = None,
        start_deployment: bool = True,
        ignore_not_found: bool = False,
    ) -> Cluster:
        assert self._client
        try:
            url = self._endpoints.storage(cluster_name, storage_name)
            headers = self._create_headers(token=token)
            async with self._client.delete(
                url.with_query(start_deployment=str(start_deployment).lower()),
                headers=headers,
            ) as response:
                response.raise_for_status()
                resp_payload = await response.json()
                return self._entity_factory.create_cluster(resp_payload)
        except ClientResponseError as e:
            if not ignore_not_found or e.status != 404:
                raise
        return await self.get_cluster(cluster_name)

    async def get_node_pool(
        self,
        cluster_name: str,
        node_pool_name: str,
        *,
        token: str | None = None,
    ) -> NodePool:
        assert self._client

        url = self._endpoints.node_pool(cluster_name, node_pool_name)
        headers = self._create_headers(token=token)
        async with self._client.get(url=url, headers=headers) as response:
            response.raise_for_status()
            resp_payload = await response.json()
            return self._entity_factory.create_node_pool(resp_payload)

    async def get_node_pools(
        self, cluster_name: str, *, token: str | None = None
    ) -> list[NodePool]:
        assert self._client

        url = self._endpoints.node_pools(cluster_name)
        headers = self._create_headers(token=token)
        async with self._client.get(url=url, headers=headers) as response:
            response.raise_for_status()
            resp_payload = await response.json()
            return [self._entity_factory.create_node_pool(n) for n in resp_payload]

    async def get_node_pool_templates(
        self,
        cloud_provider_type: CloudProviderType,
        *,
        token: str | None = None,
    ) -> list[NodePoolTemplate]:
        assert self._client

        if cloud_provider_type == CloudProviderType.ON_PREM:
            raise ValueError("Templates are not supported in onprem clusters.")

        url = self._endpoints.cloud_providers / cloud_provider_type.value
        headers = self._create_headers(token=token)
        async with self._client.get(url=url, headers=headers) as response:
            response.raise_for_status()
            resp_payload = await response.json()
            np_templates = [
                self._entity_factory.create_node_pool_template(npt)
                for npt in resp_payload["node_pools"]
            ]
            return np_templates

    async def add_node_pool(
        self,
        cluster_name: str,
        node_pool: NodePool,
        *,
        token: str | None = None,
        start_deployment: bool = True,
    ) -> Cluster:
        """Add new node pool to the existing cluster.
        Cloud provider should be already set up.

        Make sure you use one of the available node pool templates by providing its ID,
            if the cluster is deployed in public cloud (AWS / GCP / Azure / VCD).

        Args:
            cluster_name (str): Name of the cluster within the platform.
            node_pool (NodePool): Node pool instance.
                For templates, you could use template.to_node_pool() method
            token (str | None, optional): User token to perform changes.
                Should has write access to cluster://{cluster_name}/cloud_provider role.
            start_deployment (bool, optional): Start applying changes. Defaults to True.

        Returns:
            Cluster: Cluster instance with applied changes
        """
        assert self._client

        url = self._endpoints.node_pools(cluster_name)
        headers = self._create_headers(token=token)
        payload = self._payload_factory.create_node_pool(node_pool)
        async with self._client.post(
            url.with_query(start_deployment=str(start_deployment).lower()),
            headers=headers,
            json=payload,
        ) as response:
            response.raise_for_status()
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def put_node_pool(
        self,
        cluster_name: str,
        node_pool: NodePool,
        *,
        token: str | None = None,
        start_deployment: bool = True,
    ) -> Cluster:
        assert self._client

        url = self._endpoints.node_pool(cluster_name, node_pool.name)
        headers = self._create_headers(token=token)
        payload = self._payload_factory.create_node_pool(node_pool)

        async with self._client.put(
            url.with_query(start_deployment=str(start_deployment).lower()),
            headers=headers,
            json=payload,
        ) as response:
            response.raise_for_status()
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def patch_node_pool(
        self,
        cluster_name: str,
        node_pool_name: str,
        *,
        idle_size: int | None = None,
        token: str | None = None,
    ) -> Cluster:
        assert self._client

        url = self._endpoints.node_pool(cluster_name, node_pool_name)
        headers = self._create_headers(token=token)
        payload: dict[str, Any] = {}
        if idle_size is not None:
            payload["idle_size"] = idle_size

        async with self._client.patch(url, headers=headers, json=payload) as response:
            response.raise_for_status()
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def delete_node_pool(
        self,
        cluster_name: str,
        node_pool_name: str,
        *,
        token: str | None = None,
        start_deployment: bool = True,
    ) -> Cluster:
        assert self._client

        url = self._endpoints.node_pool(cluster_name, node_pool_name)
        headers = self._create_headers(token=token)
        async with self._client.delete(
            url.with_query(start_deployment=str(start_deployment).lower()),
            headers=headers,
        ) as response:
            response.raise_for_status()
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def notify(
        self,
        cluster_name: str,
        notification_type: NotificationType,
        message: str | None = None,
        *,
        token: str | None = None,
    ) -> None:
        assert self._client

        url = self._endpoints.notifications(cluster_name)
        headers = self._create_headers(token=token)
        payload = {"notification_type": notification_type.value}
        if message:
            payload["message"] = message
        async with self._client.post(url, headers=headers, json=payload) as response:
            response.raise_for_status()

    async def get_resource_presets(
        self, cluster_name: str, *, token: str | None = None
    ) -> list[ResourcePreset]:
        assert self._client

        url = self._endpoints.resource_presets(cluster_name)
        headers = self._create_headers(token=token)
        async with self._client.get(url, headers=headers) as response:
            response.raise_for_status()
            resp_payload = await response.json()
            return [
                self._entity_factory.create_resource_preset(p) for p in resp_payload
            ]

    async def get_resource_preset(
        self, cluster_name: str, preset_name: str, *, token: str | None = None
    ) -> ResourcePreset:
        assert self._client

        url = self._endpoints.resource_preset(cluster_name, preset_name)
        headers = self._create_headers(token=token)
        async with self._client.get(url, headers=headers) as response:
            response.raise_for_status()
            resp_payload = await response.json()
            return self._entity_factory.create_resource_preset(resp_payload)

    async def add_resource_preset(
        self, cluster_name: str, preset: ResourcePreset, *, token: str | None = None
    ) -> Cluster:
        assert self._client

        url = self._endpoints.resource_presets(cluster_name)
        headers = self._create_headers(token=token)
        payload = self._payload_factory.create_resource_preset(preset)
        async with self._client.post(url, headers=headers, json=payload) as response:
            response.raise_for_status()
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def put_resource_preset(
        self, cluster_name: str, preset: ResourcePreset, *, token: str | None = None
    ) -> Cluster:
        assert self._client

        url = self._endpoints.resource_preset(cluster_name, preset.name)
        headers = self._create_headers(token=token)
        payload = self._payload_factory.create_resource_preset(preset)
        async with self._client.put(url, headers=headers, json=payload) as response:
            response.raise_for_status()
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def delete_resource_preset(
        self, cluster_name: str, preset_name: str, *, token: str | None = None
    ) -> Cluster:
        assert self._client

        url = self._endpoints.resource_preset(cluster_name, preset_name)
        headers = self._create_headers(token=token)
        async with self._client.delete(url, headers=headers) as response:
            response.raise_for_status()
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)
