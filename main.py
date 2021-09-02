num = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciseis', 'diecisiete', 'dieciocho', 'diecinueve']
num2 = ['', '', 'veinti', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta' ,'ochenta', 'noventa']
num3 = ['', 'ciento', 'doscientos', 'trescientos', 'cuatroscientos', 'quinientos', 'seiscientos', 'sietecientos' , 'ochocientos', 'novecientos']
num4 = ['', 'mil', 'millon', 'millardo']

number = input('Ingrese un valor numerico positivo: ')

def twoDigitsBuilder(number):
	try:
		digit = str(number)[0]
		digit2 = str(number)[1]
	except:
		pass
	if number < 20:
		return num[number]
	if number == 20:
		return 'veinte'
	if number > 20 and number < 100:
		digit = str(number)[0]
		digit2 = str(number)[1]
		return num2[int(digit)]+ ' ' + num[int(digit2)]
	

def hundredBuilder(number):
	try:
		digit = str(number)[0]
		digit3 = str(number)[2]
		digit2 = str(number)[1]
	except:
		pass

	if number < 1:
		return ''

	if number > 0 and number < 100:
		return twoDigitsBuilder(number)
	if number >= 100 and number < 1000:
		if number == 100:
			return 'cien'
		if (digit2 == '1'):
			digit2 = str(number)[1] + str(number)[2]
			return num3[int(digit)] + ' ' + num[int(digit2)]	
		return num3[int(digit)] + ' ' + num2[int(digit2)] + ' ' + num[int(digit3)]


def sixDigitsBuilder(number):
	if number < 1000:
		return ''
	if number >= 1000 and number < 10000000:
		
		if len(str(number)) == 4:
			numbers =  str(number)[0] 
			hundreds = str(number)[1] + str(number)[2] + str(number)[3]

		elif len(str(number)) == 5:
			numbers=  str(number)[0] + str(number)[1]
			hundreds = str(number)[2] + str(number)[3] + str(number)[4]

		elif len(str(number)) == 6:
			numbers =  str(number)[0] + str(number)[1] + str(number) [2]
			hundreds = str(number)[3] + str(number)[4] + str(number)[5]

		firstThree = str(hundredBuilder(int(numbers)))

		if number >= 1000 and number <= 1999:	
			return num4[1] + ' ' + str(hundredBuilder(int(hundreds))	)
		
		return firstThree + ' ' + num4[1] + ' ' + str(hundredBuilder(int(hundreds)))
	

def numberToWords(number):
	try:
		number = int(number)
		if number < 0:
			return 'Expresion incorrecta'	
	except:
		return 'Expresion incorrecta'	
	
	if number == 0:
		return 'cero'

	if number >= 1 and number < 1000:
		return hundredBuilder(number)
	
	if number >= 1000 and number < 1000000:
		return sixDigitsBuilder(number)
	
	if number >= 1000000 and number < 1000000000:
		if len(str(number)) == 7:
			firstDigits = str(number)[:1]
		if len(str(number)) == 8:
			firstDigits = str(number)[:2]
		if len(str(number)) == 9:
			firstDigits = str(number)[:3]
		lastDigits = sixDigitsBuilder(int(str(number)[-6::]))
		return hundredBuilder(int(firstDigits)) + ' ' + num4[2] + ' ' + str(lastDigits)
	
	if number == 1000000000:
		return 'un millardo'
	return 'Andate a cagar'
	

wordedNumber = numberToWords(number)
print(wordedNumber)