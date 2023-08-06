from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopChannel")


@attr.s(auto_attribs=True)
class TopChannel:
    """
    Attributes:
        id (Union[Unset, str]):
        type (Union[Unset, str]):
        display_name (Union[Unset, str]):
        name (Union[Unset, str]):
        team_id (Union[Unset, str]):
        message_count (Union[Unset, str]): The number of messages posted in the channel by users over the given time
            period (not including messages posted by bots).
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    team_id: Union[Unset, str] = UNSET
    message_count: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        display_name = self.display_name
        name = self.name
        team_id = self.team_id
        message_count = self.message_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if message_count is not UNSET:
            field_dict["message_count"] = message_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        display_name = d.pop("display_name", UNSET)

        name = d.pop("name", UNSET)

        team_id = d.pop("team_id", UNSET)

        message_count = d.pop("message_count", UNSET)

        top_channel = cls(
            id=id,
            type=type,
            display_name=display_name,
            name=name,
            team_id=team_id,
            message_count=message_count,
        )

        top_channel.additional_properties = d
        return top_channel

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
