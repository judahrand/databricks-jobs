from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.azure_attributes_availability import AzureAttributesAvailability
from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureAttributes")


@attr.s(auto_attribs=True)
class AzureAttributes:
    """
    Attributes:
        first_on_demand (Union[Unset, int]): The first `first_on_demand` nodes of the cluster are placed on on-demand
            instances. This value must be greater than 0, or else cluster creation validation fails. If this value is
            greater than or equal to the current cluster size, all nodes are placed on on-demand instances. If this value is
            less than the current cluster size, `first_on_demand` nodes are placed on on-demand instances and the remainder
            are placed on availability instances. This value does not affect cluster size and cannot be mutated over the
            lifetime of a cluster.
        availability (Union[Unset, AzureAttributesAvailability]): Availability type used for all subsequent nodes past
            the `first_on_demand` ones.

            `SPOT_AZURE`: use spot instances.
            `ON_DEMAND_AZURE`: use on demand instances.
            `SPOT_WITH_FALLBACK_AZURE`: preferably use spot instances, but fall back to on-demand instances if spot
            instances cannot be acquired (for example, if Azure spot prices are too high or out of quota). Does not apply to
            pool availability.
        spot_bid_max_price (Union[Unset, float]): The max bid price used for Azure spot instances. You can set this to
            greater than or equal to the current spot price. You can also set this to -1 (the default), which specifies that
            the instance cannot be evicted on the basis of price. The price for the instance is the current price for spot
            instances or the price for a standard instance. You can view historical pricing and eviction rates in the Azure
            portal.
    """

    first_on_demand: Union[Unset, int] = UNSET
    availability: Union[Unset, AzureAttributesAvailability] = UNSET
    spot_bid_max_price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_on_demand = self.first_on_demand
        availability: Union[Unset, str] = UNSET
        if not isinstance(self.availability, Unset):
            availability = self.availability.value

        spot_bid_max_price = self.spot_bid_max_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_on_demand is not UNSET:
            field_dict["first_on_demand"] = first_on_demand
        if availability is not UNSET:
            field_dict["availability"] = availability
        if spot_bid_max_price is not UNSET:
            field_dict["spot_bid_max_price"] = spot_bid_max_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_on_demand = d.pop("first_on_demand", UNSET)

        _availability = d.pop("availability", UNSET)
        availability: Union[Unset, AzureAttributesAvailability]
        if isinstance(_availability, Unset):
            availability = UNSET
        else:
            availability = AzureAttributesAvailability(_availability)

        spot_bid_max_price = d.pop("spot_bid_max_price", UNSET)

        azure_attributes = cls(
            first_on_demand=first_on_demand,
            availability=availability,
            spot_bid_max_price=spot_bid_max_price,
        )

        azure_attributes.additional_properties = d
        return azure_attributes

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
