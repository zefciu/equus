from nose.tools import assert_equal, assert_is_none

from tests.shared import SampleNestedConfiguration


def test_all_params():
    config = SampleNestedConfiguration({
        'required_str_param': 'spam',
        'optional_str_param': 'eggs',
        'default_str_param': 'sausage',
        'required_int_param': 42,
        'subconfiguration': {
            'url': 'http://example.com',
            'pool_size': 5,
        }
    })
    assert_equal(config.required_str_param, 'spam')
    assert_equal(config.optional_str_param, 'eggs')
    assert_equal(config.default_str_param, 'sausage')
    assert_equal(config.required_int_param, 42)
    assert_equal(config.subconfiguration.url, 'http://example.com')


def test_optional_params():
    config = SampleNestedConfiguration({
        'required_str_param': 'spam',
        'required_int_param': 42,
        'subconfiguration': {
            'url': 'http://example.com',
            'pool_size': 5,
        }
    })
    assert_equal(config.required_str_param, 'spam')
    assert_is_none(config.optional_str_param)
    assert_equal(config.default_str_param, 'bacon')
    assert_equal(config.required_int_param, 42)
    assert_equal(config.subconfiguration.url, 'http://example.com')
