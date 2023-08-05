import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointOut")


@attr.s(auto_attribs=True)
class EndpointOut:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):  Example: ep_1srOrx2ZWZBpBUvZwXKQmoEYga2.
        updated_at (datetime.datetime):
        url (str):  Example: https://example.com/webhook/.
        version (int):  Example: 1.
        channels (Union[Unset, None, List[str]]): List of message channels this endpoint listens to (omit for all)
            Example: ['project_123', 'group_2'].
        description (Union[Unset, str]):  Default: ''. Example: An example endpoint name.
        disabled (Union[Unset, bool]):
        filter_types (Union[Unset, None, List[str]]):  Example: ['user.signup', 'user.deleted'].
        rate_limit (Union[Unset, None, int]):  Example: 1000.
        uid (Union[Unset, None, str]): Optional unique identifier for the endpoint Example: unique-endpoint-identifier.
    """

    created_at: datetime.datetime
    id: str
    updated_at: datetime.datetime
    url: str
    version: int
    channels: Union[Unset, None, List[str]] = UNSET
    description: Union[Unset, str] = ""
    disabled: Union[Unset, bool] = False
    filter_types: Union[Unset, None, List[str]] = UNSET
    rate_limit: Union[Unset, None, int] = UNSET
    uid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id
        updated_at = self.updated_at.isoformat()

        url = self.url
        version = self.version
        channels: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.channels, Unset):
            if self.channels is None:
                channels = None
            else:
                channels = self.channels

        description = self.description
        disabled = self.disabled
        filter_types: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.filter_types, Unset):
            if self.filter_types is None:
                filter_types = None
            else:
                filter_types = self.filter_types

        rate_limit = self.rate_limit
        uid = self.uid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "updatedAt": updated_at,
                "url": url,
                "version": version,
            }
        )
        if channels is not UNSET:
            field_dict["channels"] = channels
        if description is not UNSET:
            field_dict["description"] = description
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if filter_types is not UNSET:
            field_dict["filterTypes"] = filter_types
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

        updated_at = isoparse(dict_copy.pop("updatedAt"))

        url = dict_copy.pop("url")

        version = dict_copy.pop("version")

        channels = cast(List[str], dict_copy.pop("channels", UNSET))

        description = dict_copy.pop("description", UNSET)

        disabled = dict_copy.pop("disabled", UNSET)

        filter_types = cast(List[str], dict_copy.pop("filterTypes", UNSET))

        rate_limit = dict_copy.pop("rateLimit", UNSET)

        uid = dict_copy.pop("uid", UNSET)

        endpoint_out = cls(
            created_at=created_at,
            id=id,
            updated_at=updated_at,
            url=url,
            version=version,
            channels=channels,
            description=description,
            disabled=disabled,
            filter_types=filter_types,
            rate_limit=rate_limit,
            uid=uid,
        )

        endpoint_out.additional_properties = dict_copy
        return endpoint_out

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
