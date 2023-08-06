from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.channel import Channel
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchAllChannelsResponse200")


@attr.s(auto_attribs=True)
class SearchAllChannelsResponse200:
    """
    Attributes:
        channels (Union[Unset, List[Channel]]): The channels that matched the query.
        total_count (Union[Unset, float]): The total number of results, regardless of page and per_page requested.
    """

    channels: Union[Unset, List[Channel]] = UNSET
    total_count: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()

                channels.append(channels_item)

        total_count = self.total_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channels = []
        _channels = d.pop("channels", UNSET)
        for channels_item_data in _channels or []:
            channels_item = Channel.from_dict(channels_item_data)

            channels.append(channels_item)

        total_count = d.pop("total_count", UNSET)

        search_all_channels_response_200 = cls(
            channels=channels,
            total_count=total_count,
        )

        search_all_channels_response_200.additional_properties = d
        return search_all_channels_response_200

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
