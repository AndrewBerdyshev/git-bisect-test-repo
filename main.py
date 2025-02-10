def sum(a, b):
    return a + b + 1

def test1(capsys):
    assert sum(1, 2) == 3

# python3 -m pytest main.py