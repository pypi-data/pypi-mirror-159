from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="UpdateTeamPrivacyJsonBody")


@attr.s(auto_attribs=True)
class UpdateTeamPrivacyJsonBody:
    """
    Attributes:
        privacy (str): Team privacy setting: 'O' for a public (open) team, 'I' for a private (invitation only) team
    """

    privacy: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        privacy = self.privacy

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "privacy": privacy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        privacy = d.pop("privacy")

        update_team_privacy_json_body = cls(
            privacy=privacy,
        )

        update_team_privacy_json_body.additional_properties = d
        return update_team_privacy_json_body

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
