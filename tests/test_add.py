from src.math_oper import add_two

def test_add_two():
    assert add_two(3,5) == 8
    assert add_two(2,5) == 7
    assert add_two(1,5) == 6
    