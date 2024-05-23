# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .converted_format import ConvertedFormat
from .export_status import ExportStatus
from .user_simple import UserSimple


class Export(pydantic_v1.BaseModel):
    title: typing.Optional[str] = None
    id: typing.Optional[int] = None
    created_by: typing.Optional[UserSimple] = None
    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    Creation time
    """

    finished_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    Complete or fail time
    """

    status: typing.Optional[ExportStatus] = None
    md5: typing.Optional[str] = None
    counters: typing.Optional[typing.Dict[str, typing.Any]] = None
    converted_formats: typing.Optional[typing.List[ConvertedFormat]] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
