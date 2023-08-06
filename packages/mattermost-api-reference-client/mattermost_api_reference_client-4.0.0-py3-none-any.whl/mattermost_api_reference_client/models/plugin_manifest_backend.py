from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginManifestBackend")


@attr.s(auto_attribs=True)
class PluginManifestBackend:
    """Deprecated in Mattermost 5.2 release.

    Attributes:
        executable (Union[Unset, str]): Path to the executable binary.
    """

    executable: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        executable = self.executable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if executable is not UNSET:
            field_dict["executable"] = executable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        executable = d.pop("executable", UNSET)

        plugin_manifest_backend = cls(
            executable=executable,
        )

        plugin_manifest_backend.additional_properties = d
        return plugin_manifest_backend

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
