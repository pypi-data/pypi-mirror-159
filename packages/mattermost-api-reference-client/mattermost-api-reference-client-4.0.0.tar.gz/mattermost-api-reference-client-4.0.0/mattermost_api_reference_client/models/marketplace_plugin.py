from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.plugin_manifest import PluginManifest
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketplacePlugin")


@attr.s(auto_attribs=True)
class MarketplacePlugin:
    """
    Attributes:
        homepage_url (Union[Unset, str]): URL that leads to the homepage of the plugin.
        icon_data (Union[Unset, str]): Base64 encoding of a plugin icon SVG.
        download_url (Union[Unset, str]): URL to download the plugin.
        release_notes_url (Union[Unset, str]): URL that leads to the release notes of the plugin.
        labels (Union[Unset, List[str]]): A list of the plugin labels.
        signature (Union[Unset, str]): Base64 encoded signature of the plugin.
        manifest (Union[Unset, PluginManifest]):
        installed_version (Union[Unset, str]): Version number of the already installed plugin, if any.
    """

    homepage_url: Union[Unset, str] = UNSET
    icon_data: Union[Unset, str] = UNSET
    download_url: Union[Unset, str] = UNSET
    release_notes_url: Union[Unset, str] = UNSET
    labels: Union[Unset, List[str]] = UNSET
    signature: Union[Unset, str] = UNSET
    manifest: Union[Unset, PluginManifest] = UNSET
    installed_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        homepage_url = self.homepage_url
        icon_data = self.icon_data
        download_url = self.download_url
        release_notes_url = self.release_notes_url
        labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        signature = self.signature
        manifest: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.manifest, Unset):
            manifest = self.manifest.to_dict()

        installed_version = self.installed_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if homepage_url is not UNSET:
            field_dict["homepage_url"] = homepage_url
        if icon_data is not UNSET:
            field_dict["icon_data"] = icon_data
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if release_notes_url is not UNSET:
            field_dict["release_notes_url"] = release_notes_url
        if labels is not UNSET:
            field_dict["labels"] = labels
        if signature is not UNSET:
            field_dict["signature"] = signature
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if installed_version is not UNSET:
            field_dict["installed_version"] = installed_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        homepage_url = d.pop("homepage_url", UNSET)

        icon_data = d.pop("icon_data", UNSET)

        download_url = d.pop("download_url", UNSET)

        release_notes_url = d.pop("release_notes_url", UNSET)

        labels = cast(List[str], d.pop("labels", UNSET))

        signature = d.pop("signature", UNSET)

        _manifest = d.pop("manifest", UNSET)
        manifest: Union[Unset, PluginManifest]
        if isinstance(_manifest, Unset):
            manifest = UNSET
        else:
            manifest = PluginManifest.from_dict(_manifest)

        installed_version = d.pop("installed_version", UNSET)

        marketplace_plugin = cls(
            homepage_url=homepage_url,
            icon_data=icon_data,
            download_url=download_url,
            release_notes_url=release_notes_url,
            labels=labels,
            signature=signature,
            manifest=manifest,
            installed_version=installed_version,
        )

        marketplace_plugin.additional_properties = d
        return marketplace_plugin

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
