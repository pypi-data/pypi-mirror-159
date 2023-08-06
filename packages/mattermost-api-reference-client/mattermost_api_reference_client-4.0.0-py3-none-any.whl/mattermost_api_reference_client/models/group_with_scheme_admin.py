from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.group import Group
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupWithSchemeAdmin")


@attr.s(auto_attribs=True)
class GroupWithSchemeAdmin:
    """group augmented with scheme admin information

    Attributes:
        group (Union[Unset, Group]):
        scheme_admin (Union[Unset, bool]):
    """

    group: Union[Unset, Group] = UNSET
    scheme_admin: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        scheme_admin = self.scheme_admin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if scheme_admin is not UNSET:
            field_dict["scheme_admin"] = scheme_admin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _group = d.pop("group", UNSET)
        group: Union[Unset, Group]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = Group.from_dict(_group)

        scheme_admin = d.pop("scheme_admin", UNSET)

        group_with_scheme_admin = cls(
            group=group,
            scheme_admin=scheme_admin,
        )

        group_with_scheme_admin.additional_properties = d
        return group_with_scheme_admin

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
