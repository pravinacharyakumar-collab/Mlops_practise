from calculator import add, subtract


def test_add():
    assert add(30, 20) == 50


def test_subtract():
    assert subtract(30, 20) == 10
