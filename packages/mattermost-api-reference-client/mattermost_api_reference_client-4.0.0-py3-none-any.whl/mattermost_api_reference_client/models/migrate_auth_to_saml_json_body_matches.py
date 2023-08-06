from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="MigrateAuthToSamlJsonBodyMatches")


@attr.s(auto_attribs=True)
class MigrateAuthToSamlJsonBodyMatches:
    """Users map."""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        migrate_auth_to_saml_json_body_matches = cls()

        migrate_auth_to_saml_json_body_matches.additional_properties = d
        return migrate_auth_to_saml_json_body_matches

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
