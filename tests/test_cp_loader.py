import io

from nose.tools import assert_equal

from tests.shared import SampleFlatConfiguration

CONFIGURATION_FULL_DATA = io.StringIO("""
[app_config]
required_str_param: spam
optional_str_param: eggs
default_str_param: sausage
required_int_param: 42
""")


CONFIGURATION_PARTIAL_DATA = io.StringIO("""
[app_config]
required_str_param: spam
required_int_param: 42
""")


CONFIGURATION_YAML = io.StringIO("""
---
required_str_param: spam
optional_str_param: eggs
default_str_param: sausage
""")


def test_load_full_data():
    config = SampleFlatConfiguration.load((CONFIGURATION_FULL_DATA, 'app_config'))
    assert_equal(config.required_str_param, 'spam')
    assert_equal(config.optional_str_param, 'eggs')
    assert_equal(config.default_str_param, 'sausage')
    assert_equal(config.required_int_param, 42)
