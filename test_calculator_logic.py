import сalculator_logic as c
import pytest


def test_add():
    assert c.add(10,5)==15
    assert c.add(-1,1)==0
    assert c.add(-2, -2) == -4

    with pytest.raises(TypeError): # обрататывает исключения
        c.add('text',5)
    with pytest.raises(TypeError):
        c.add(4,'text')


def test_subtract():
    assert c.subtract(10,5)==5
    assert c.subtract(-1, 1)==-2
    assert c.subtract(-10,-10)==0

    with pytest.raises(TypeError): # обрататывает исключения
        c.subtract('text',5)
    with pytest.raises(TypeError):
        c.subtract(4,'text')


def test_multiply():
    assert c.multiply(2,2)==4
    assert c.multiply(-5,6)==-30
    assert c.multiply(-1,-5)==5


def test_divide():
    assert c.divide(10,2)==5
    assert c.divide(-10, 2) == -5
    assert c.divide(-10, -2) == 5

    with pytest.raises(TypeError): # обрататывает исключения
        c.divide('text',5)
    with pytest.raises(TypeError):
        c.divide(4,'text')
    with pytest.raises(ZeroDivisionError):
        c.divide(4,0)



test_add()
test_subtract()
test_multiply()
test_divide()

print('Тесты пройдены успешно')