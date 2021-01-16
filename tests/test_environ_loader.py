from os import environ
from nose.tools import assert_equal

from equus.loaders.environ import EnvironInput
from tests.shared import SampleFlatConfiguration


environ['CONFIG_required_str_param'] = 'spam'
environ['CONFIG_optional_str_param'] = 'eggs'
environ['CONFIG_default_str_param'] = 'sausage'
environ['CONFIG_required_int_param'] = '42'


def test_load_data():
    config = SampleFlatConfiguration.load(EnvironInput('CONFIG_'))
    assert_equal(config.required_str_param, 'spam')
    assert_equal(config.optional_str_param, 'eggs')
    assert_equal(config.default_str_param, 'sausage')
    assert_equal(config.required_int_param, 42)
