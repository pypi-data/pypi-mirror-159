from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="UpdateTeamSchemeJsonBody")


@attr.s(auto_attribs=True)
class UpdateTeamSchemeJsonBody:
    """
    Attributes:
        scheme_id (str): The ID of the scheme.
    """

    scheme_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scheme_id = self.scheme_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheme_id": scheme_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scheme_id = d.pop("scheme_id")

        update_team_scheme_json_body = cls(
            scheme_id=scheme_id,
        )

        update_team_scheme_json_body.additional_properties = d
        return update_team_scheme_json_body

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
