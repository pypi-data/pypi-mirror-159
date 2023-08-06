from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ExecuteCommandJsonBody")


@attr.s(auto_attribs=True)
class ExecuteCommandJsonBody:
    """
    Attributes:
        channel_id (str): Channel Id where the command will execute
        command (str): The slash command to execute
    """

    channel_id: str
    command: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_id = self.channel_id
        command = self.command

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "command": command,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = d.pop("channel_id")

        command = d.pop("command")

        execute_command_json_body = cls(
            channel_id=channel_id,
            command=command,
        )

        execute_command_json_body.additional_properties = d
        return execute_command_json_body

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
