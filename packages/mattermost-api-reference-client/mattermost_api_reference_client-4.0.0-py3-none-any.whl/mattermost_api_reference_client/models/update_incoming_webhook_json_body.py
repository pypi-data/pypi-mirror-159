from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncomingWebhookJsonBody")


@attr.s(auto_attribs=True)
class UpdateIncomingWebhookJsonBody:
    """
    Attributes:
        channel_id (str): The ID of a public channel or private group that receives the webhook payloads.
        display_name (str): The display name for this incoming webhook
        description (str): The description for this incoming webhook
        hook_id (Union[Unset, str]): Incoming webhook GUID
        username (Union[Unset, str]): The username this incoming webhook will post as.
        icon_url (Union[Unset, str]): The profile picture this incoming webhook will use when posting.
    """

    channel_id: str
    display_name: str
    description: str
    hook_id: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    icon_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_id = self.channel_id
        display_name = self.display_name
        description = self.description
        hook_id = self.hook_id
        username = self.username
        icon_url = self.icon_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "display_name": display_name,
                "description": description,
            }
        )
        if hook_id is not UNSET:
            field_dict["hook_id"] = hook_id
        if username is not UNSET:
            field_dict["username"] = username
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = d.pop("channel_id")

        display_name = d.pop("display_name")

        description = d.pop("description")

        hook_id = d.pop("hook_id", UNSET)

        username = d.pop("username", UNSET)

        icon_url = d.pop("icon_url", UNSET)

        update_incoming_webhook_json_body = cls(
            channel_id=channel_id,
            display_name=display_name,
            description=description,
            hook_id=hook_id,
            username=username,
            icon_url=icon_url,
        )

        update_incoming_webhook_json_body.additional_properties = d
        return update_incoming_webhook_json_body

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
