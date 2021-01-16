import io
from os import environ

from equus.loaders.environ import EnvironInput
from tests.shared import SubConfig, SampleNestedConfiguration


environ['SUB_url'] = 'http://example.com'
environ['SUB_pool_size'] = '5'


MAIN_INI = io.StringIO("""[app_config]
required_str_param: spam
optional_str_param: eggs
default_str_param: sausage
required_int_param: 42
""")


def test_combine():
    subconfig = SubConfig.load(EnvironInput('SUB_'))
    config = SampleNestedConfiguration.load(
        (MAIN_INI, 'app_config'),
        subconfiguration=subconfig,
    )