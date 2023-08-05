from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.message_endpoint_out import MessageEndpointOut
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListResponseMessageEndpointOut")


@attr.s(auto_attribs=True)
class ListResponseMessageEndpointOut:
    """
    Attributes:
        data (List[MessageEndpointOut]):
        done (bool):
        iterator (Union[Unset, None, str]):  Example: iterator.
    """

    data: List[MessageEndpointOut]
    done: bool
    iterator: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        done = self.done
        iterator = self.iterator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "done": done,
            }
        )
        if iterator is not UNSET:
            field_dict["iterator"] = iterator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        dict_copy = src_dict.copy()
        data = []
        _data = dict_copy.pop("data")
        for data_item_data in _data:
            data_item = MessageEndpointOut.from_dict(data_item_data)

            data.append(data_item)

        done = dict_copy.pop("done")

        iterator = dict_copy.pop("iterator", UNSET)

        list_response_message_endpoint_out = cls(
            data=data,
            done=done,
            iterator=iterator,
        )

        list_response_message_endpoint_out.additional_properties = dict_copy
        return list_response_message_endpoint_out

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
