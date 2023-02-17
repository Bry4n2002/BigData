from funcion import sumar,primo
def test_sumar():
    assert sumar(2,4) == 6

def test_primo():
    assert primo(5) is True
    assert primo(4) is False
    
	
