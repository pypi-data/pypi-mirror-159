from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.plugin_manifest import PluginManifest
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPluginsResponse200")


@attr.s(auto_attribs=True)
class GetPluginsResponse200:
    """
    Attributes:
        active (Union[Unset, List[PluginManifest]]):
        inactive (Union[Unset, List[PluginManifest]]):
    """

    active: Union[Unset, List[PluginManifest]] = UNSET
    inactive: Union[Unset, List[PluginManifest]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.active, Unset):
            active = []
            for active_item_data in self.active:
                active_item = active_item_data.to_dict()

                active.append(active_item)

        inactive: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inactive, Unset):
            inactive = []
            for inactive_item_data in self.inactive:
                inactive_item = inactive_item_data.to_dict()

                inactive.append(inactive_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if inactive is not UNSET:
            field_dict["inactive"] = inactive

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active = []
        _active = d.pop("active", UNSET)
        for active_item_data in _active or []:
            active_item = PluginManifest.from_dict(active_item_data)

            active.append(active_item)

        inactive = []
        _inactive = d.pop("inactive", UNSET)
        for inactive_item_data in _inactive or []:
            inactive_item = PluginManifest.from_dict(inactive_item_data)

            inactive.append(inactive_item)

        get_plugins_response_200 = cls(
            active=active,
            inactive=inactive,
        )

        get_plugins_response_200.additional_properties = d
        return get_plugins_response_200

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
