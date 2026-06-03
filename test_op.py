from op import add, subtract, multiply, divide


def test_add():
    a = 10
    b = 5
    assert add(a,b) == 15


def test_subtract():
    a=10
    b=5
    assert subtract(a,b)==5

def test_multiply():
    a=10
    b=5
    assert multiply(a,b)== 5

def test_divide():
    a=10
    b=5
    assert divide(a,b)==3
