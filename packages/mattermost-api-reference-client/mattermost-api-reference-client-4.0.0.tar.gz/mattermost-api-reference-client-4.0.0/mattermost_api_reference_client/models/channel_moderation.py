from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.channel_moderated_roles import ChannelModeratedRoles
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelModeration")


@attr.s(auto_attribs=True)
class ChannelModeration:
    """
    Attributes:
        name (Union[Unset, str]):
        roles (Union[Unset, ChannelModeratedRoles]):
    """

    name: Union[Unset, str] = UNSET
    roles: Union[Unset, ChannelModeratedRoles] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        roles: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _roles = d.pop("roles", UNSET)
        roles: Union[Unset, ChannelModeratedRoles]
        if isinstance(_roles, Unset):
            roles = UNSET
        else:
            roles = ChannelModeratedRoles.from_dict(_roles)

        channel_moderation = cls(
            name=name,
            roles=roles,
        )

        channel_moderation.additional_properties = d
        return channel_moderation

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
