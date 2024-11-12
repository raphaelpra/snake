from helpers import syracuse

def test_syracuse_even():
    assert syracuse(4) == 2

def test_syracuse_odd():
    assert syracuse(5) == 16