from typing import Optional

from equus.configuration import Configuration


class SubConfig(Configuration):
    url: str
    pool_size: int


class SampleNestedConfiguration(Configuration):
    required_str_param: str
    optional_str_param: Optional[str]
    default_str_param: str = 'bacon'
    required_int_param: int
    subconfiguration: SubConfig


class SampleFlatConfiguration(Configuration):
    required_str_param: str
    optional_str_param: Optional[str]
    default_str_param: str = 'bacon'
    required_int_param: int
