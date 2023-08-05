# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: unacast/v2/metric/dimension.proto, unacast/v2/metric/metric_value.proto, unacast/v2/metric/metric_report.proto, unacast/v2/metric/lens.proto, unacast/v2/metric/metric.proto, unacast/v2/metric/metric_group.proto, unacast/v2/metric/metric_service.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
import grpclib


class Cadence(betterproto.Enum):
    CADENCE_UNSPECIFIED = 0
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3
    QUARTERLY = 4
    YEARLY = 5
    TRIMONTHLY = 6


class ValueKind(betterproto.Enum):
    KIND_UNSPECIFIED = 0
    NUMBER = 1
    COUNT = 2
    CATEGORY = 3


class LifecycleStage(betterproto.Enum):
    UNSPECIFIED = 0
    PROTOTYPE = 3
    RELEASE_CANDIDATE = 6
    STABLE = 9
    DEPRECATED = 12
    ARCHIVED = 15
    DELETED = 18


class ColumnKind(betterproto.Enum):
    VALUE = 0
    DISPLAY_NAME = 1
    GEOMETRY = 2


@dataclass(eq=False, repr=False)
class Dimension(betterproto.Message):
    name: str = betterproto.string_field(4)
    dimension_id: str = betterproto.string_field(1)
    catalog_id: str = betterproto.string_field(2)
    display_name: str = betterproto.string_field(5)
    description: str = betterproto.string_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DimensionValue(betterproto.Message):
    # @exclude @inject_tag: `bigquery:"dimension_id"`
    dimension_id: str = betterproto.string_field(1)
    # @exclude @inject_tag: `bigquery:"value"`
    value: str = betterproto.string_field(2)
    # @exclude @inject_tag: `bigquery:"display_name"`
    display_name: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DimensionFilter(betterproto.Message):
    dimension_id: str = betterproto.string_field(1)
    values: List[str] = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MapFeatureRef(betterproto.Message):
    layer_id: str = betterproto.string_field(1)
    feature_id: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricValue(betterproto.Message):
    # @exclude @inject_tag: `bigquery:"dimension_id"`
    metric_id: str = betterproto.string_field(1)
    # @exclude @inject_tag: `bigquery:"value"`
    observation_period: "Period" = betterproto.message_field(3)
    # @exclude @inject_tag: `bigquery:"display_name"`
    map_feature_v2: "_maps__.Feature" = betterproto.message_field(9)
    related_map_feature: "_maps__.Feature" = betterproto.message_field(5)
    dimensions: List["DimensionValue"] = betterproto.message_field(6)
    supporting_values: List["MetricValueValue"] = betterproto.message_field(7)
    value: "MetricValueValue" = betterproto.message_field(2)
    flags: List["MetricValueFlag"] = betterproto.message_field(8)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricValueValue(betterproto.Message):
    name: str = betterproto.string_field(1)
    unit: str = betterproto.string_field(2)
    number: float = betterproto.float_field(9, group="value")
    count: int = betterproto.int64_field(10, group="value")
    category: str = betterproto.string_field(11, group="value")

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricValueFlag(betterproto.Message):
    code: str = betterproto.string_field(1)
    display_name: str = betterproto.string_field(2)
    detail: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Period(betterproto.Message):
    start: "__unatype__.Date" = betterproto.message_field(1)
    end: "__unatype__.Date" = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricReport(betterproto.Message):
    observation_period: "Period" = betterproto.message_field(3)
    total_size: int = betterproto.int32_field(4)
    address_components: List["AddressComponentReport"] = betterproto.message_field(5)
    value_p1: float = betterproto.float_field(6)
    value_p5: float = betterproto.float_field(7)
    value_p25: float = betterproto.float_field(8)
    value_p50: float = betterproto.float_field(9)
    value_p75: float = betterproto.float_field(10)
    value_p95: float = betterproto.float_field(11)
    value_p99: float = betterproto.float_field(12)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddressComponentReport(betterproto.Message):
    # @exclude @inject_tag: `bigquery:"dimension_id"`
    component: str = betterproto.string_field(1)
    # @exclude @inject_tag: `bigquery:"value"`
    cardinality: int = betterproto.int32_field(2)
    # @exclude @inject_tag: `bigquery:"display_name"`
    short_name: str = betterproto.string_field(3)
    display_name: str = betterproto.string_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Lens(betterproto.Message):
    id: str = betterproto.string_field(1)
    catalog_id: str = betterproto.string_field(2)
    metric_id: str = betterproto.string_field(3)
    billing_account_id: str = betterproto.string_field(4)
    creator_email: str = betterproto.string_field(5)
    lens_filters: "LensFilters" = betterproto.message_field(6)
    display_name: str = betterproto.string_field(10)
    description: str = betterproto.string_field(11)
    update_time_string: str = betterproto.string_field(13)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class LensFilters(betterproto.Message):
    # @exclude @inject_tag: `bigquery:"dimension_id"`
    period_filters: List["Period"] = betterproto.message_field(1)
    # @exclude @inject_tag: `bigquery:"value"`
    dimension_filters: List["DimensionFilter"] = betterproto.message_field(2)
    # @exclude @inject_tag: `bigquery:"display_name"`
    address_component_filters: List[
        "_maps__.AddressComponentFilter"
    ] = betterproto.message_field(3)
    feature_filters: List[str] = betterproto.string_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Metric(betterproto.Message):
    id: str = betterproto.string_field(1)
    catalog_id: str = betterproto.string_field(2)
    display_name: str = betterproto.string_field(3)
    description: str = betterproto.string_field(4)
    spec: "MetricSpec" = betterproto.message_field(6)
    metric_versions: List["MetricVersion"] = betterproto.message_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricVersion(betterproto.Message):
    # @exclude @inject_tag: `bigquery:"dimension_id"`
    id: str = betterproto.string_field(1)
    # @exclude @inject_tag: `bigquery:"value"`
    catalog_id: str = betterproto.string_field(2)
    # @exclude @inject_tag: `bigquery:"display_name"`
    description: str = betterproto.string_field(4)
    lifecycle_stage: "LifecycleStage" = betterproto.enum_field(9)
    version_spec: "VersionSpec" = betterproto.message_field(18)
    spec: "MetricVersionSpec" = betterproto.message_field(5)
    layer_id: str = betterproto.string_field(6)
    layer: "_maps__.Layer" = betterproto.message_field(8)
    related_layer_id: str = betterproto.string_field(12)
    related_layer: "_maps__.Layer" = betterproto.message_field(13)
    dimensions: List["Dimension"] = betterproto.message_field(7)
    listing: str = betterproto.string_field(11)
    availability: "__unatype__.AvailabilityKind" = betterproto.enum_field(22)
    report: "MetricReport" = betterproto.message_field(14)
    your_subscription: "_subscription__.SubscriptionStatus" = betterproto.message_field(
        15
    )
    your_lens: "Lens" = betterproto.message_field(17)
    index_update_time: str = betterproto.string_field(20)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricSpec(betterproto.Message):
    tags: List["TagSpec"] = betterproto.message_field(8)
    groups: List[str] = betterproto.string_field(9)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class TagSpec(betterproto.Message):
    type: str = betterproto.string_field(1)
    values: List[str] = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricVersionSpec(betterproto.Message):
    layer_id: str = betterproto.string_field(1)
    related_layer_id: str = betterproto.string_field(2)
    relation_type: str = betterproto.string_field(10)
    cadence: "Cadence" = betterproto.enum_field(4)
    dimensions: List["DimensionSpec"] = betterproto.message_field(5)
    values: List["ValueSpec"] = betterproto.message_field(7)
    value_kind: "ValueKind" = betterproto.enum_field(3)
    unit: str = betterproto.string_field(6)
    group_memberships: List["GroupMemberSpec"] = betterproto.message_field(8)
    processing_cadence: "Cadence" = betterproto.enum_field(9)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GroupMemberSpec(betterproto.Message):
    key: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class VersionSpec(betterproto.Message):
    version: str = betterproto.string_field(1)
    release_notes: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DimensionSpec(betterproto.Message):
    dimension_id: str = betterproto.string_field(1)
    default_value: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ValueSpec(betterproto.Message):
    name: str = betterproto.string_field(1)
    value_kind: "ValueKind" = betterproto.enum_field(2)
    unit: str = betterproto.string_field(3)
    display_name: str = betterproto.string_field(4)
    description: str = betterproto.string_field(5)
    supporting_value: bool = betterproto.bool_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Value(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class LeanMetricVersion(betterproto.Message):
    id: str = betterproto.string_field(1)
    catalog_id: str = betterproto.string_field(2)
    description: str = betterproto.string_field(4)
    lifecycle_stage: "LifecycleStage" = betterproto.enum_field(9)
    version_spec: "VersionSpec" = betterproto.message_field(18)
    listing: str = betterproto.string_field(11)
    availability: "__unatype__.AvailabilityKind" = betterproto.enum_field(20)
    your_subscription: "_subscription__.SubscriptionStatus" = betterproto.message_field(
        15
    )
    spec: "LeanMetricVersionSpec" = betterproto.message_field(19)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class LeanMetricVersionSpec(betterproto.Message):
    cadence: "Cadence" = betterproto.enum_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class LeanMetric(betterproto.Message):
    id: str = betterproto.string_field(1)
    catalog_id: str = betterproto.string_field(2)
    display_name: str = betterproto.string_field(3)
    description: str = betterproto.string_field(4)
    spec: "MetricSpec" = betterproto.message_field(6)
    metric_versions: List["LeanMetricVersion"] = betterproto.message_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DataSchema(betterproto.Message):
    observation_start_column: "Column" = betterproto.message_field(1)
    observation_end_column: "Column" = betterproto.message_field(2)
    feature_columns: List["Column"] = betterproto.message_field(3)
    related_feature_columns: List["Column"] = betterproto.message_field(4)
    address_component_columns: List["Column"] = betterproto.message_field(5)
    related_address_component_columns: List["Column"] = betterproto.message_field(6)
    dimension_columns: List["Column"] = betterproto.message_field(7)
    values_columns: List["Column"] = betterproto.message_field(8)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Column(betterproto.Message):
    id: str = betterproto.string_field(1)
    type: "ColumnKind" = betterproto.enum_field(2)
    default_name: str = betterproto.string_field(3)
    user_friendly_name: str = betterproto.string_field(4)
    description: str = betterproto.string_field(5)
    format: str = betterproto.string_field(6)
    is_included: bool = betterproto.bool_field(7)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MetricGroup(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    metric_id: str = betterproto.string_field(2)
    key: str = betterproto.string_field(3)
    key_display_name: str = betterproto.string_field(4)
    possible_values: "PossibleValues" = betterproto.message_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class PossibleValues(betterproto.Message):
    # @exclude @inject_tag: `bigquery:"dimension_id"`
    ids: List[str] = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class UpdateMetricRequest(betterproto.Message):
    metric: "Metric" = betterproto.message_field(1)
    update_mask: "betterproto_lib_google_protobuf.FieldMask" = (
        betterproto.message_field(2)
    )
    billing_context: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetDefaultDataSchemaRequest(betterproto.Message):
    # @exclude @inject_tag: `bigquery:"dimension_id"`
    catalog_id: str = betterproto.string_field(1)
    # @exclude @inject_tag: `bigquery:"value"`
    metric_id: str = betterproto.string_field(2)
    # @exclude @inject_tag: `bigquery:"display_name"`
    billing_account_id: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetDefaultDataSchemaResponse(betterproto.Message):
    data_schema: "DataSchema" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetMetricGroupsRequest(betterproto.Message):
    metric_id: str = betterproto.string_field(1)
    catalog_id: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetMetricGroupsResponse(betterproto.Message):
    groups: List["MetricGroup"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


class MetricServiceStub(betterproto.ServiceStub):
    async def update_metric(
        self,
        *,
        metric: "Metric" = None,
        update_mask: "betterproto_lib_google_protobuf.FieldMask" = None,
        billing_context: str = "",
    ) -> "Metric":

        request = UpdateMetricRequest()
        if metric is not None:
            request.metric = metric
        if update_mask is not None:
            request.update_mask = update_mask
        request.billing_context = billing_context

        return await self._unary_unary(
            "/unacast.v2.metric.MetricService/UpdateMetric", request, Metric
        )

    async def get_default_data_schema(
        self, *, catalog_id: str = "", metric_id: str = "", billing_account_id: str = ""
    ) -> "GetDefaultDataSchemaResponse":

        request = GetDefaultDataSchemaRequest()
        request.catalog_id = catalog_id
        request.metric_id = metric_id
        request.billing_account_id = billing_account_id

        return await self._unary_unary(
            "/unacast.v2.metric.MetricService/GetDefaultDataSchema",
            request,
            GetDefaultDataSchemaResponse,
        )

    async def get_metric_groups(
        self, *, metric_id: str = "", catalog_id: str = ""
    ) -> "GetMetricGroupsResponse":

        request = GetMetricGroupsRequest()
        request.metric_id = metric_id
        request.catalog_id = catalog_id

        return await self._unary_unary(
            "/unacast.v2.metric.MetricService/GetMetricGroups",
            request,
            GetMetricGroupsResponse,
        )


from .. import maps as _maps__
from .. import subscription as _subscription__
from ... import unatype as __unatype__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
