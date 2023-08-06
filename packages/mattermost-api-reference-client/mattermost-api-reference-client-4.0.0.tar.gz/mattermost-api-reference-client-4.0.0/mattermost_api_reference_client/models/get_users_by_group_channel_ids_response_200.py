from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user import User
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUsersByGroupChannelIdsResponse200")


@attr.s(auto_attribs=True)
class GetUsersByGroupChannelIdsResponse200:
    """
    Attributes:
        channel_id (Union[Unset, List[User]]):
    """

    channel_id: Union[Unset, List[User]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_id: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = []
            for channel_id_item_data in self.channel_id:
                channel_id_item = channel_id_item_data.to_dict()

                channel_id.append(channel_id_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["<CHANNEL_ID>"] = channel_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = []
        _channel_id = d.pop("<CHANNEL_ID>", UNSET)
        for channel_id_item_data in _channel_id or []:
            channel_id_item = User.from_dict(channel_id_item_data)

            channel_id.append(channel_id_item)

        get_users_by_group_channel_ids_response_200 = cls(
            channel_id=channel_id,
        )

        get_users_by_group_channel_ids_response_200.additional_properties = d
        return get_users_by_group_channel_ids_response_200

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
