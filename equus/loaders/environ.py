from dataclasses import dataclass
from os import environ
from typing import Any


@dataclass
class EnvironInput:
    prefix: str


def environ_loader(input_: Any):
    if not isinstance(input_, EnvironInput):
        raise TypeError('Not an EnvironInput')
    prefix = input_.prefix
    result = {}
    for name in environ:
        if not name.startswith(prefix):
            continue
        trunc_name = name[len(prefix):]
        result[trunc_name] = environ[name]
    return result
