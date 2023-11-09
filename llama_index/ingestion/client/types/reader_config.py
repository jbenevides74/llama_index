# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from llama_index.ingestion.client.core.datetime_utils import serialize_datetime

from .base_pydantic_reader import BasePydanticReader


class ReaderConfig(pydantic.BaseModel):
    """
    Represents a reader and it's input arguments.
    """

    reader: BasePydanticReader = pydantic.Field(description="Reader to use.")
    reader_args: typing.Optional[typing.List[typing.Any]] = pydantic.Field(
        description="Reader args."
    )
    reader_kwargs: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description="Reader kwargs."
    )
    class_name: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}