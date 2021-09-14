from main import numberToWords

def test_92():
	assert numberToWords(92) == 'noventa dos'

def test_109():
	assert numberToWords(109) == 'ciento nueve'

def test_34223():
	assert numberToWords(34223) == 'treinta cuatro mil doscientos veinti tres'


def test_420():
	assert numberToWords(420) == 'cuatrocientos veinti'

def test_421():
	assert numberToWords(421) == 'cuatrocientos veinti uno'

def test_982323():
	assert numberToWords(982323) == 'novecientos ochenta dos mil trescientos veinti tres'

def test_0():
	assert numberToWords(0) == 'cero'

def test_asd():
	assert numberToWords('asd') == 'Expresión inválida'