from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.top_channel import TopChannel
from ..types import UNSET, Unset

T = TypeVar("T", bound="TopChannelList")


@attr.s(auto_attribs=True)
class TopChannelList:
    """
    Attributes:
        has_next (Union[Unset, bool]): Indicates if there is another page of channels that can be fetched.
        items (Union[Unset, List[TopChannel]]): List of channels.
    """

    has_next: Union[Unset, bool] = UNSET
    items: Union[Unset, List[TopChannel]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        has_next = self.has_next
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_next is not UNSET:
            field_dict["has_next"] = has_next
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        has_next = d.pop("has_next", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = TopChannel.from_dict(items_item_data)

            items.append(items_item)

        top_channel_list = cls(
            has_next=has_next,
            items=items,
        )

        top_channel_list.additional_properties = d
        return top_channel_list

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
