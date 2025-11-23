from src.calculadora import sumar, restar


def test_sumar_v2():
    assert sumar(2, 3) == 5


def test_restar_v2():
    assert restar(5, 2) == 3
