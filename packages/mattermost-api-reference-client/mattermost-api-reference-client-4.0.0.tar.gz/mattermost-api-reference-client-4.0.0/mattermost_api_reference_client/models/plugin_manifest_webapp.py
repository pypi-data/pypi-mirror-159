from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginManifestWebapp")


@attr.s(auto_attribs=True)
class PluginManifestWebapp:
    """
    Attributes:
        bundle_path (Union[Unset, str]): Path to the webapp JavaScript bundle.
    """

    bundle_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bundle_path = self.bundle_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bundle_path is not UNSET:
            field_dict["bundle_path"] = bundle_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bundle_path = d.pop("bundle_path", UNSET)

        plugin_manifest_webapp = cls(
            bundle_path=bundle_path,
        )

        plugin_manifest_webapp.additional_properties = d
        return plugin_manifest_webapp

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
