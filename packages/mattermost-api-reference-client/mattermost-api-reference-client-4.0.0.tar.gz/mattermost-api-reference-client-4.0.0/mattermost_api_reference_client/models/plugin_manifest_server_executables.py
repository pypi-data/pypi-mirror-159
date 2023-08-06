from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginManifestServerExecutables")


@attr.s(auto_attribs=True)
class PluginManifestServerExecutables:
    """Paths to executable binaries, specifying multiple entry points for different platforms when bundled together in a
    single plugin.

        Attributes:
            linux_amd64 (Union[Unset, str]):
            darwin_amd64 (Union[Unset, str]):
            windows_amd64 (Union[Unset, str]):
    """

    linux_amd64: Union[Unset, str] = UNSET
    darwin_amd64: Union[Unset, str] = UNSET
    windows_amd64: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        linux_amd64 = self.linux_amd64
        darwin_amd64 = self.darwin_amd64
        windows_amd64 = self.windows_amd64

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linux_amd64 is not UNSET:
            field_dict["linux-amd64"] = linux_amd64
        if darwin_amd64 is not UNSET:
            field_dict["darwin-amd64"] = darwin_amd64
        if windows_amd64 is not UNSET:
            field_dict["windows-amd64"] = windows_amd64

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        linux_amd64 = d.pop("linux-amd64", UNSET)

        darwin_amd64 = d.pop("darwin-amd64", UNSET)

        windows_amd64 = d.pop("windows-amd64", UNSET)

        plugin_manifest_server_executables = cls(
            linux_amd64=linux_amd64,
            darwin_amd64=darwin_amd64,
            windows_amd64=windows_amd64,
        )

        plugin_manifest_server_executables.additional_properties = d
        return plugin_manifest_server_executables

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
