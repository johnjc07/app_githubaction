from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert sub(5,3)==2

def test_sub():
    assert sub(8,3)==5
    assert add(6,3)==3
    assert add(4,5)==-1
