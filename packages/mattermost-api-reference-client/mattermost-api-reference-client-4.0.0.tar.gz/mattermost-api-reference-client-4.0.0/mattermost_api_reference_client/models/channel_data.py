from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.channel import Channel
from ..models.channel_member import ChannelMember
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelData")


@attr.s(auto_attribs=True)
class ChannelData:
    """
    Attributes:
        channel (Union[Unset, Channel]):
        member (Union[Unset, ChannelMember]):
    """

    channel: Union[Unset, Channel] = UNSET
    member: Union[Unset, ChannelMember] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.to_dict()

        member: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.member, Unset):
            member = self.member.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if member is not UNSET:
            field_dict["member"] = member

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _channel = d.pop("channel", UNSET)
        channel: Union[Unset, Channel]
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = Channel.from_dict(_channel)

        _member = d.pop("member", UNSET)
        member: Union[Unset, ChannelMember]
        if isinstance(_member, Unset):
            member = UNSET
        else:
            member = ChannelMember.from_dict(_member)

        channel_data = cls(
            channel=channel,
            member=member,
        )

        channel_data.additional_properties = d
        return channel_data

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
