# content of __init__.py
def inc(x):
    return x + 1


def test_inc():
    assert inc(3) == 4

def test_negative():
    assert not inc(3) == 4