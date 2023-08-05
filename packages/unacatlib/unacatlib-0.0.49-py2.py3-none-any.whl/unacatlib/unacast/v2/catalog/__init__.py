# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: unacast/v2/catalog/catalog.proto, unacast/v2/catalog/data_delivery_service.proto, unacast/v2/catalog/catalog_service.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
import grpclib


class DestinationConfigType(betterproto.Enum):
    BIG_QUERY_DST = 0
    GCS = 1
    S3 = 2


class DataDeliveryStatusType(betterproto.Enum):
    ENABLED = 0
    DISABLED = 1


@dataclass(eq=False, repr=False)
class Catalog(betterproto.Message):
    id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class CreateDataDeliveryRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    metric_id: str = betterproto.string_field(2)
    billing_context: str = betterproto.string_field(4)
    filters: "DataDeliveryFilters" = betterproto.message_field(5)
    data_schema_changes: "_metric__.DataSchema" = betterproto.message_field(6)
    big_query_destination: "BigQueryDestination" = betterproto.message_field(
        11, group="destination"
    )
    file_destination: "FileDestination" = betterproto.message_field(
        12, group="destination"
    )

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class CreateDataDeliveryResponse(betterproto.Message):
    delivery: "DataDelivery" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetDataDeliveryStatusRequest(betterproto.Message):
    id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetDataDeliveryStatusResponse(betterproto.Message):
    id: str = betterproto.string_field(1)
    event_id: str = betterproto.string_field(3)
    status: "__index_v1__.IndexStatus" = betterproto.enum_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class PauseDataDeliveryRequest(betterproto.Message):
    data_delivery_id: str = betterproto.string_field(1)
    billing_context: str = betterproto.string_field(2)
    catalog_id: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class PauseDataDeliveryResponse(betterproto.Message):
    delivery: "DataDelivery" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ResumeDataDeliveryRequest(betterproto.Message):
    data_delivery_id: str = betterproto.string_field(1)
    billing_context: str = betterproto.string_field(2)
    catalog_id: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ResumeDataDeliveryResponse(betterproto.Message):
    delivery: "DataDelivery" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListDataDeliveriesRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    billing_context: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListDataDeliveriesResponse(betterproto.Message):
    deliveries: List["DataDelivery"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DataDelivery(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    metric_id: str = betterproto.string_field(2)
    billing_account_id: str = betterproto.string_field(3)
    id: str = betterproto.string_field(10)
    filters: "DataDeliveryFilters" = betterproto.message_field(4)
    destination_config_json: str = betterproto.string_field(6)
    destination_config_type: "DestinationConfigType" = betterproto.enum_field(7)
    data_schema: "_metric__.DataSchema" = betterproto.message_field(8)
    status: "DataDeliveryStatusType" = betterproto.enum_field(9)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DataDeliveryFilters(betterproto.Message):
    feature_filter: List[str] = betterproto.string_field(1)
    address_component_filter: List[
        "_maps__.AddressComponentFilter"
    ] = betterproto.message_field(2)
    dimension_filter: List["_metric__.DimensionFilter"] = betterproto.message_field(3)
    start_date: "__unatype__.Date" = betterproto.message_field(4)
    end_date: "__unatype__.Date" = betterproto.message_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class BigQueryDestination(betterproto.Message):
    project_id: str = betterproto.string_field(1)
    dataset_id: str = betterproto.string_field(2)
    table_id: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class FileConfig(betterproto.Message):
    filename: str = betterproto.string_field(1)
    format: str = betterproto.string_field(2)
    compression: str = betterproto.string_field(3)
    field_delimiter: str = betterproto.string_field(4)
    header: bool = betterproto.bool_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GcsDestination(betterproto.Message):
    bucket: str = betterproto.string_field(1)
    path: str = betterproto.string_field(2)
    region: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class S3Destination(betterproto.Message):
    bucket: str = betterproto.string_field(1)
    path: str = betterproto.string_field(2)
    region: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class FileDestination(betterproto.Message):
    file_config: "FileConfig" = betterproto.message_field(2)
    s3_destination: "S3Destination" = betterproto.message_field(
        5, group="bucket_config"
    )
    gcs_destination: "GcsDestination" = betterproto.message_field(
        6, group="bucket_config"
    )

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetCatalogRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListCatalogsRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListCatalogsResponse(betterproto.Message):
    catalogs: List["Catalog"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetMetricRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    metric_id: str = betterproto.string_field(2)
    billing_context: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetMetricResponse(betterproto.Message):
    metric: "_metric__.Metric" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListMetricsRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    billing_context: str = betterproto.string_field(2)
    layer_filter: List[str] = betterproto.string_field(5)
    product_filter: List[str] = betterproto.string_field(16)
    availability_filter: List["__unatype__.AvailabilityKind"] = betterproto.enum_field(
        6
    )
    group_filter: List["_metric__.GroupMemberSpec"] = betterproto.message_field(7)
    page_size: int = betterproto.int32_field(14)
    page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListMetricsResponse(betterproto.Message):
    metrics: List["_metric__.Metric"] = betterproto.message_field(1)
    next_page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListMetricsLeanResponse(betterproto.Message):
    metrics: List["_metric__.LeanMetric"] = betterproto.message_field(1)
    next_page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetLayerRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    layer_id: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetLayerResponse(betterproto.Message):
    layer: "_maps__.Layer" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListProductsRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListProductsResponse(betterproto.Message):
    products: List[str] = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class QueryLayerRequest(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    layer_id: str = betterproto.string_field(2)
    address_component_filter: List[
        "_maps__.AddressComponentFilter"
    ] = betterproto.message_field(5)
    page_size: int = betterproto.int32_field(14)
    page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class QueryLayerResponse(betterproto.Message):
    features: List["_maps__.Feature"] = betterproto.message_field(4)
    total_size: int = betterproto.int32_field(14)
    next_page_token: str = betterproto.string_field(15)

    def __post_init__(self) -> None:
        super().__post_init__()


class DataDeliveryServiceStub(betterproto.ServiceStub):
    async def create_data_delivery(
        self,
        *,
        catalog_id: str = "",
        metric_id: str = "",
        billing_context: str = "",
        filters: "DataDeliveryFilters" = None,
        data_schema_changes: "_metric__.DataSchema" = None,
        big_query_destination: "BigQueryDestination" = None,
        file_destination: "FileDestination" = None,
    ) -> "CreateDataDeliveryResponse":

        request = CreateDataDeliveryRequest()
        request.catalog_id = catalog_id
        request.metric_id = metric_id
        request.billing_context = billing_context
        if filters is not None:
            request.filters = filters
        if data_schema_changes is not None:
            request.data_schema_changes = data_schema_changes
        if big_query_destination is not None:
            request.big_query_destination = big_query_destination
        if file_destination is not None:
            request.file_destination = file_destination

        return await self._unary_unary(
            "/unacast.v2.catalog.DataDeliveryService/CreateDataDelivery",
            request,
            CreateDataDeliveryResponse,
        )

    async def get_data_delivery_status(
        self, *, id: str = ""
    ) -> "GetDataDeliveryStatusResponse":

        request = GetDataDeliveryStatusRequest()
        request.id = id

        return await self._unary_unary(
            "/unacast.v2.catalog.DataDeliveryService/GetDataDeliveryStatus",
            request,
            GetDataDeliveryStatusResponse,
        )

    async def pause_data_delivery(
        self,
        *,
        data_delivery_id: str = "",
        billing_context: str = "",
        catalog_id: str = "",
    ) -> "PauseDataDeliveryResponse":

        request = PauseDataDeliveryRequest()
        request.data_delivery_id = data_delivery_id
        request.billing_context = billing_context
        request.catalog_id = catalog_id

        return await self._unary_unary(
            "/unacast.v2.catalog.DataDeliveryService/PauseDataDelivery",
            request,
            PauseDataDeliveryResponse,
        )

    async def resume_data_delivery(
        self,
        *,
        data_delivery_id: str = "",
        billing_context: str = "",
        catalog_id: str = "",
    ) -> "ResumeDataDeliveryResponse":

        request = ResumeDataDeliveryRequest()
        request.data_delivery_id = data_delivery_id
        request.billing_context = billing_context
        request.catalog_id = catalog_id

        return await self._unary_unary(
            "/unacast.v2.catalog.DataDeliveryService/ResumeDataDelivery",
            request,
            ResumeDataDeliveryResponse,
        )

    async def list_data_deliveries(
        self, *, catalog_id: str = "", billing_context: str = ""
    ) -> "ListDataDeliveriesResponse":

        request = ListDataDeliveriesRequest()
        request.catalog_id = catalog_id
        request.billing_context = billing_context

        return await self._unary_unary(
            "/unacast.v2.catalog.DataDeliveryService/ListDataDeliveries",
            request,
            ListDataDeliveriesResponse,
        )


class CatalogServiceStub(betterproto.ServiceStub):
    async def list_catalogs(self) -> "ListCatalogsResponse":

        request = ListCatalogsRequest()

        return await self._unary_unary(
            "/unacast.v2.catalog.CatalogService/ListCatalogs",
            request,
            ListCatalogsResponse,
        )

    async def get_metric(
        self, *, catalog_id: str = "", metric_id: str = "", billing_context: str = ""
    ) -> "GetMetricResponse":

        request = GetMetricRequest()
        request.catalog_id = catalog_id
        request.metric_id = metric_id
        request.billing_context = billing_context

        return await self._unary_unary(
            "/unacast.v2.catalog.CatalogService/GetMetric", request, GetMetricResponse
        )

    async def list_metrics(
        self,
        *,
        catalog_id: str = "",
        billing_context: str = "",
        layer_filter: Optional[List[str]] = None,
        product_filter: Optional[List[str]] = None,
        availability_filter: Optional[List["__unatype__.AvailabilityKind"]] = None,
        group_filter: Optional[List["_metric__.GroupMemberSpec"]] = None,
        page_size: int = 0,
        page_token: str = "",
    ) -> "ListMetricsResponse":
        layer_filter = layer_filter or []
        product_filter = product_filter or []
        availability_filter = availability_filter or []
        group_filter = group_filter or []

        request = ListMetricsRequest()
        request.catalog_id = catalog_id
        request.billing_context = billing_context
        request.layer_filter = layer_filter
        request.product_filter = product_filter
        request.availability_filter = availability_filter
        if group_filter is not None:
            request.group_filter = group_filter
        request.page_size = page_size
        request.page_token = page_token

        return await self._unary_unary(
            "/unacast.v2.catalog.CatalogService/ListMetrics",
            request,
            ListMetricsResponse,
        )

    async def list_metrics_lean(
        self,
        *,
        catalog_id: str = "",
        billing_context: str = "",
        layer_filter: Optional[List[str]] = None,
        product_filter: Optional[List[str]] = None,
        availability_filter: Optional[List["__unatype__.AvailabilityKind"]] = None,
        group_filter: Optional[List["_metric__.GroupMemberSpec"]] = None,
        page_size: int = 0,
        page_token: str = "",
    ) -> "ListMetricsLeanResponse":
        layer_filter = layer_filter or []
        product_filter = product_filter or []
        availability_filter = availability_filter or []
        group_filter = group_filter or []

        request = ListMetricsRequest()
        request.catalog_id = catalog_id
        request.billing_context = billing_context
        request.layer_filter = layer_filter
        request.product_filter = product_filter
        request.availability_filter = availability_filter
        if group_filter is not None:
            request.group_filter = group_filter
        request.page_size = page_size
        request.page_token = page_token

        return await self._unary_unary(
            "/unacast.v2.catalog.CatalogService/ListMetricsLean",
            request,
            ListMetricsLeanResponse,
        )

    async def get_layer(
        self, *, catalog_id: str = "", layer_id: str = ""
    ) -> "GetLayerResponse":

        request = GetLayerRequest()
        request.catalog_id = catalog_id
        request.layer_id = layer_id

        return await self._unary_unary(
            "/unacast.v2.catalog.CatalogService/GetLayer", request, GetLayerResponse
        )

    async def list_products(self) -> "ListProductsResponse":

        request = ListProductsRequest()

        return await self._unary_unary(
            "/unacast.v2.catalog.CatalogService/ListProducts",
            request,
            ListProductsResponse,
        )


from .. import maps as _maps__
from .. import metric as _metric__
from ... import unatype as __unatype__
from ...index import v1 as __index_v1__
