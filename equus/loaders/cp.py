import io
import typing
from configparser import ConfigParser
from typing import Any


def config_parser_loader(input_: Any) -> typing.Mapping[str, Any]:
    parser = ConfigParser()
    section = None
    if isinstance(input_, str):
        if ':' in input_:
            filename, _, section = input_.partition(':')
        else:
            filename = input_
        parser.read(filename)
    elif isinstance(input_, io.IOBase):
        parser.read_file(input_)
    elif isinstance(input_, tuple):
        if len(input_) != 2:
            raise TypeError('Input unrecognized')
        file_, section = input_
        if not isinstance(file_, io.IOBase):
            raise TypeError('Input unrecognized')
        parser.read_file(file_)
    else:
        raise TypeError('Input unrecognized')
    if section:
        return parser[section]
    else:
        return parser
