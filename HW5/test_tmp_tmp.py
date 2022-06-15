import pytest

@pytest.mark.xfail
def test_some_test():
    assert 1 > 10
