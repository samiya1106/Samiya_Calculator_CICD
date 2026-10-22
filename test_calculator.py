from calculator import add, subtract, multiply, divide, square

def test_add():
    assert add(2, 3) == 8

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_square():
    assert square(4) == 16

