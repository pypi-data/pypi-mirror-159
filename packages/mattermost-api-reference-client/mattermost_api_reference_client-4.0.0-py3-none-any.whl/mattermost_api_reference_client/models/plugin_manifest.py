from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.plugin_manifest_backend import PluginManifestBackend
from ..models.plugin_manifest_server import PluginManifestServer
from ..models.plugin_manifest_settings_schema import PluginManifestSettingsSchema
from ..models.plugin_manifest_webapp import PluginManifestWebapp
from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginManifest")


@attr.s(auto_attribs=True)
class PluginManifest:
    """
    Attributes:
        id (Union[Unset, str]): Globally unique identifier that represents the plugin.
        name (Union[Unset, str]): Name of the plugin.
        description (Union[Unset, str]): Description of what the plugin is and does.
        version (Union[Unset, str]): Version number of the plugin.
        min_server_version (Union[Unset, str]): The minimum Mattermost server version required for the plugin.

            Available as server version 5.6.
        backend (Union[Unset, PluginManifestBackend]): Deprecated in Mattermost 5.2 release.
        server (Union[Unset, PluginManifestServer]):
        webapp (Union[Unset, PluginManifestWebapp]):
        settings_schema (Union[Unset, PluginManifestSettingsSchema]): Settings schema used to define the System Console
            UI for the plugin.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    min_server_version: Union[Unset, str] = UNSET
    backend: Union[Unset, PluginManifestBackend] = UNSET
    server: Union[Unset, PluginManifestServer] = UNSET
    webapp: Union[Unset, PluginManifestWebapp] = UNSET
    settings_schema: Union[Unset, PluginManifestSettingsSchema] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        version = self.version
        min_server_version = self.min_server_version
        backend: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.backend, Unset):
            backend = self.backend.to_dict()

        server: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        webapp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.webapp, Unset):
            webapp = self.webapp.to_dict()

        settings_schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings_schema, Unset):
            settings_schema = self.settings_schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if version is not UNSET:
            field_dict["version"] = version
        if min_server_version is not UNSET:
            field_dict["min_server_version"] = min_server_version
        if backend is not UNSET:
            field_dict["backend"] = backend
        if server is not UNSET:
            field_dict["server"] = server
        if webapp is not UNSET:
            field_dict["webapp"] = webapp
        if settings_schema is not UNSET:
            field_dict["settings_schema"] = settings_schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        version = d.pop("version", UNSET)

        min_server_version = d.pop("min_server_version", UNSET)

        _backend = d.pop("backend", UNSET)
        backend: Union[Unset, PluginManifestBackend]
        if isinstance(_backend, Unset):
            backend = UNSET
        else:
            backend = PluginManifestBackend.from_dict(_backend)

        _server = d.pop("server", UNSET)
        server: Union[Unset, PluginManifestServer]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = PluginManifestServer.from_dict(_server)

        _webapp = d.pop("webapp", UNSET)
        webapp: Union[Unset, PluginManifestWebapp]
        if isinstance(_webapp, Unset):
            webapp = UNSET
        else:
            webapp = PluginManifestWebapp.from_dict(_webapp)

        _settings_schema = d.pop("settings_schema", UNSET)
        settings_schema: Union[Unset, PluginManifestSettingsSchema]
        if isinstance(_settings_schema, Unset):
            settings_schema = UNSET
        else:
            settings_schema = PluginManifestSettingsSchema.from_dict(_settings_schema)

        plugin_manifest = cls(
            id=id,
            name=name,
            description=description,
            version=version,
            min_server_version=min_server_version,
            backend=backend,
            server=server,
            webapp=webapp,
            settings_schema=settings_schema,
        )

        plugin_manifest.additional_properties = d
        return plugin_manifest

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
