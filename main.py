from builders import *

def numberToWords(number):
	try:
		number = int(number)
		if number < 0:
			return 'Expresión inválida'	
	except:
		return 'Expresión inválida'	
	
	if number == 0:
		return 'cero'
	if number >= 1 and number < 1000:
		return hundredBuilder(number)
	if number >= 1000 and number < 1000000:
		return sixDigitsBuilder(number)
	if number >= 1000000 and number < 1000000000:
		return sevenDigitsBuilder(number)
	if number == 1000000000:
		return 'un millardo'
	return 'Andate a cagar'
	
try:
	numero = input('Ingrese un valor numerico positivo: ')
	print(numberToWords(numero))
except:
	print('error')