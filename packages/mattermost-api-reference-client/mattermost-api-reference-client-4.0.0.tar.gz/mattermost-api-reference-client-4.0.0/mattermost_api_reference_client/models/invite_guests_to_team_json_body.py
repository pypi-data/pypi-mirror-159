from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InviteGuestsToTeamJsonBody")


@attr.s(auto_attribs=True)
class InviteGuestsToTeamJsonBody:
    """
    Attributes:
        emails (List[str]): List of emails
        channels (List[str]): List of channel ids
        message (Union[Unset, str]): Message to include in the invite
    """

    emails: List[str]
    channels: List[str]
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        emails = self.emails

        channels = self.channels

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emails": emails,
                "channels": channels,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        emails = cast(List[str], d.pop("emails"))

        channels = cast(List[str], d.pop("channels"))

        message = d.pop("message", UNSET)

        invite_guests_to_team_json_body = cls(
            emails=emails,
            channels=channels,
            message=message,
        )

        invite_guests_to_team_json_body.additional_properties = d
        return invite_guests_to_team_json_body

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
