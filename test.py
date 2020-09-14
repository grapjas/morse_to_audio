print("Enter some text to create Morse code audio:")
text = input()

test = all(x.isalpha() or x.isspace() for x in text)
print(test)

#while (all(x.isalpha() or x.isspace() for x in text) != [True for x in text]):
#	print('Valid text is alphanumeric and spaces: ')
#	text = input()
