import pytest

def f():
    raise SystemExit(1)


def test_mytest(capsys):
    with pytest.raises(SystemExit):
        return f()