import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationOut")


@attr.s(auto_attribs=True)
class ApplicationOut:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):  Example: app_1srOrx2ZWZBpBUvZwXKQmoEYga2.
        name (str):  Example: My first application.
        updated_at (datetime.datetime):
        rate_limit (Union[Unset, None, int]):  Example: 1000.
        uid (Union[Unset, None, str]): Optional unique identifier for the application Example: unique-app-identifier.
    """

    created_at: datetime.datetime
    id: str
    name: str
    updated_at: datetime.datetime
    rate_limit: Union[Unset, None, int] = UNSET
    uid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id
        name = self.name
        updated_at = self.updated_at.isoformat()

        rate_limit = self.rate_limit
        uid = self.uid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "name": name,
                "updatedAt": updated_at,
            }
        )
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        dict_copy = src_dict.copy()
        created_at = isoparse(dict_copy.pop("createdAt"))

        id = dict_copy.pop("id")

        name = dict_copy.pop("name")

        updated_at = isoparse(dict_copy.pop("updatedAt"))

        rate_limit = dict_copy.pop("rateLimit", UNSET)

        uid = dict_copy.pop("uid", UNSET)

        application_out = cls(
            created_at=created_at,
            id=id,
            name=name,
            updated_at=updated_at,
            rate_limit=rate_limit,
            uid=uid,
        )

        application_out.additional_properties = dict_copy
        return application_out

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
