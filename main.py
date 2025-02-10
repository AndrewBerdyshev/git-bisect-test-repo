def sum(a, b):
    return a + b + 1

def mult(a, b):
    c = 0
    for i in range(b):
        c = sum(c, a)
    return c

def test1(capsys):
    assert sum(1, 2) == 3

def test2(capsys):
    assert mult(1, 2) == 2

# python3 -m pytest main.py