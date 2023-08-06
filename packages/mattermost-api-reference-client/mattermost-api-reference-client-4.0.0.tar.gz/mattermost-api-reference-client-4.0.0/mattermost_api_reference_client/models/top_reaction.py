from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopReaction")


@attr.s(auto_attribs=True)
class TopReaction:
    """
    Attributes:
        emoji_name (Union[Unset, str]): The name of the emoji used for this reaction.
        count (Union[Unset, int]): The number of the times this emoji has been used.
    """

    emoji_name: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        emoji_name = self.emoji_name
        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if emoji_name is not UNSET:
            field_dict["emoji_name"] = emoji_name
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        emoji_name = d.pop("emoji_name", UNSET)

        count = d.pop("count", UNSET)

        top_reaction = cls(
            emoji_name=emoji_name,
            count=count,
        )

        top_reaction.additional_properties = d
        return top_reaction

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
