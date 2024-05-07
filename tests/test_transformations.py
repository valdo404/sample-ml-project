import pytest

import processing.transformations


@pytest.mark.parametrize("str, result", [
    ("a(b,)", "ab"),
    ("oz,", "oz")
])
def test_remove_parentheses(str, result):
    assert(processing.transformations.remove_specials(str) == result)
