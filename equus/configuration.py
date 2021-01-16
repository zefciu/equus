from __future__ import annotations
import logging
from copy import deepcopy

from typing import TypeVar, Optional
from pkg_resources import iter_entry_points
from typing import Any, get_type_hints, Type, Union


logger = logging.getLogger(__name__)


def _is_optional(t: Type[Any]):
    return (
        hasattr(t, '__origin__')
        and t.__origin__ == Union
        and type(None) in t.__args__
    )


class EquusMetadata:
    environ_prefix: Optional[str] = None


class ConfigurationMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.__equus__ = EquusMetadata()


class Configuration(metaclass=ConfigurationMeta):
    def __init__(self, data: dict[str, Any]):
        for k, t in get_type_hints(
            type(self),
            globals(),
            locals(),
        ).items():
            data_k = k[1:] if k.startswith('_') else k
            if data_k in data:
                value = data[data_k]
                self.set_value(k, t, value)
            elif hasattr(type(self), k):
                continue
            elif _is_optional(t):
                setattr(self, k, None)
            else:
                raise TypeError(f'Value {data_k} is required')

    def set_value(self, key: str, t: Type[Any], value: Any):
        if callable(t):
            try:
                value = t(value)
            except TypeError:
                pass    # Typing stuff is callable but actually not
        setattr(self, key, value)


    T = TypeVar('T')


    @classmethod
    def load(cls: Type[T], *inputs: list[Any], **data: dict[str, Any]) -> T:
        data = deepcopy(data)
        loaders = [
            entry_point.load()
            for entry_point in iter_entry_points('equus.loader')
        ]
        for input_ in inputs:
            for loader in loaders:
                try:
                    data |= loader(input_)
                    break
                except TypeError:
                    logger.info(f'Loader {loader} rejected input {input_}')
                    continue
            else:
                raise TypeError(
                    f'Cannot parse input {input_}. Tried loaders: {loaders}'
                )
        return cls(data)
