from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.completed_job_flow_status_modules_item_type import CompletedJobFlowStatusModulesItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompletedJobFlowStatusModulesItem")


@attr.s(auto_attribs=True)
class CompletedJobFlowStatusModulesItem:
    """ """

    type: CompletedJobFlowStatusModulesItemType
    job: Union[Unset, str] = UNSET
    event: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        job = self.job
        event = self.event

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if job is not UNSET:
            field_dict["job"] = job
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = CompletedJobFlowStatusModulesItemType(d.pop("type"))

        job = d.pop("job", UNSET)

        event = d.pop("event", UNSET)

        completed_job_flow_status_modules_item = cls(
            type=type,
            job=job,
            event=event,
        )

        completed_job_flow_status_modules_item.additional_properties = d
        return completed_job_flow_status_modules_item

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
