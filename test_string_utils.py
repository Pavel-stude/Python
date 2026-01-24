import pytest
from string_utils import StringUtils

string_utils = StringUtils()

####################### capitalize
@pytest.mark.capitalize_test
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("pavel", "Pavel")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.capitalize_test
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected



######################## trim
@pytest.mark.trim_test
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("   hello world", "hello world"),
    ("   python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.trim_test
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   123", "123"),
    ("   ...", "..."),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected



########################## contains
@pytest.mark.contains_test
@pytest.mark.positive
@pytest.mark.parametrize("input_str, simbol", [
    ("Skypro", "S",),
    ("hello world", "wor"),
    ("python", "py"),
    ("123", "1"),
    (" ..", "."),
    ("", ""),
])
def test_contains_positive(input_str, simbol):
    assert string_utils.contains(input_str, simbol) == True

@pytest.mark.contains_test
@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol", [
    ("Skypro", ".",),
    ("hello world", "py"),
    ("123", "   "),
    (" ..", "1"),
    ("", "S"),
])
def test_contains_negative(input_str, simbol):
    assert string_utils.contains(input_str, simbol) == False



######################## delete_symbol
@pytest.mark.delete_symbol_test
@pytest.mark.positive
@pytest.mark.parametrize("input_str, delete_str, expected", [
    ("skypro", "sky", "pro"),
    ("hello world","world", "hello "),
    ("python","t", "pyhon"),
])
def test_delete_symbol_positive(input_str, delete_str, expected):
    assert string_utils.delete_symbol(input_str, delete_str) == expected

@pytest.mark.delete_symbol_test
@pytest.mark.negative
@pytest.mark.parametrize("input_str, delete_str, expected", [

    ("   123", "   ", "123"),
    ("...", "..", "."),
    ("Skypro", "", "Skypro"),
])
def test_delete_symbol_negative(input_str, delete_str, expected):
    assert string_utils.delete_symbol(input_str, delete_str) == expected
