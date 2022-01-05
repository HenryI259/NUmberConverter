letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def convert(oldBase, newBase, number):
	numberChars = list(str(number))
	newNumberChars = []
	decimalNumber = 0
	if oldBase != 10:
		numberIndex = 0
		for numbers in numberChars:
			numberIndex += 1
			for letter in letters:
				if numbers == letter:
					numbers = letters.index(letter) + 10
			numbers = int(numbers)
			numbers *= oldBase ** (len(numberChars) - numberIndex)
			decimalNumber += numbers
	else:
		decimalNumber = int(number)
	if newBase != 10:
		while decimalNumber / newBase >= 1:
			remainder = decimalNumber % newBase
			newNumberChars.append(remainder)
			decimalNumber //= newBase
		newNumberChars.append(decimalNumber)
		newIndex = 0
		for newNumbers in newNumberChars:
			if newNumbers > 9:

				newNumberChars[newIndex] = letters[newNumbers - 10]
			newIndex += 1
		newNumberChars = reversed(newNumberChars)
		FinalNumber = ''
		for charecter in newNumberChars:
			FinalNumber += str(charecter)
	else:
		FinalNumber = str(decimalNumber)
	return FinalNumber

print(convert(16, 10, 'AD'))