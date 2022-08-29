# content of __init__.py
def inc(val):
    return val + 1

def test_inc():
    assert inc(3) == 4

def test_negative():
    assert inc(3) != 5
