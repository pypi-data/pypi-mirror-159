from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.plugin_manifest_server_executables import PluginManifestServerExecutables
from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginManifestServer")


@attr.s(auto_attribs=True)
class PluginManifestServer:
    """
    Attributes:
        executables (Union[Unset, PluginManifestServerExecutables]): Paths to executable binaries, specifying multiple
            entry points for different platforms when bundled together in a single plugin.
        executable (Union[Unset, str]): Path to the executable binary.
    """

    executables: Union[Unset, PluginManifestServerExecutables] = UNSET
    executable: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        executables: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.executables, Unset):
            executables = self.executables.to_dict()

        executable = self.executable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if executables is not UNSET:
            field_dict["executables"] = executables
        if executable is not UNSET:
            field_dict["executable"] = executable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _executables = d.pop("executables", UNSET)
        executables: Union[Unset, PluginManifestServerExecutables]
        if isinstance(_executables, Unset):
            executables = UNSET
        else:
            executables = PluginManifestServerExecutables.from_dict(_executables)

        executable = d.pop("executable", UNSET)

        plugin_manifest_server = cls(
            executables=executables,
            executable=executable,
        )

        plugin_manifest_server.additional_properties = d
        return plugin_manifest_server

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
