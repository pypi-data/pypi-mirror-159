from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="IntegrationKeyOut")


@attr.s(auto_attribs=True)
class IntegrationKeyOut:
    """
    Attributes:
        key (str):  Example: integsk_kV3ts5tKPNJN4Dl25cMTfUNdmabxbX0O.
    """

    key: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        dict_copy = src_dict.copy()
        key = dict_copy.pop("key")

        integration_key_out = cls(
            key=key,
        )

        integration_key_out.additional_properties = dict_copy
        return integration_key_out

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
