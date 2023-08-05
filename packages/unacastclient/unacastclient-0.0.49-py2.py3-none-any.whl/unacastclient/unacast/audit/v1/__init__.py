# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: unacast/audit/v1/metric_interaction_log.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

import betterproto


@dataclass(eq=False, repr=False)
class MetricInteractionLog(betterproto.Message):
    catalog_id: str = betterproto.string_field(1)
    metric_id: str = betterproto.string_field(2)
    billing_account_id: str = betterproto.string_field(3)
    user_email: str = betterproto.string_field(4)
    request_time: datetime = betterproto.message_field(8)
    correlation_id: str = betterproto.string_field(9)
    request_tags: Dict[str, str] = betterproto.map_field(
        15, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    request_address_component_filter: List[
        "__maps_v1__.AddressComponentFilter"
    ] = betterproto.message_field(20)
    request_observation_period_filter: "__metric_v1__.Period" = (
        betterproto.message_field(21)
    )
    request_feature_filter: List[str] = betterproto.string_field(22)
    response_values_size: int = betterproto.int32_field(29)
    response_total_size: int = betterproto.int32_field(30)

    def __post_init__(self) -> None:
        super().__post_init__()


from ...maps import v1 as __maps_v1__
from ...metric import v1 as __metric_v1__
