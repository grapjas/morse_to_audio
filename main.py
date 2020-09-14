from playsound import playsound
import time, sys

# dot2.wav = 0.10s

# Each dot or dash within a character is followed by period of signal absence, 
# called a space, equal to the dot duration. 
# The letters of a word are separated by a space of duration equal to three dots, 
# and the words are separated by a space equal to seven dots.

DOT_TIME = 0.10

def morse(txt):
	codes = {'A': '.-',    'B': '-...',   'C': '-.-.', 
			'D': '-..',    'E': '.',      'F': '..-.',
			'G': '--.',    'H': '....',   'I': '..',
			'J': '.---',   'K': '-.-',    'L': '.-..',
			'M': '--',     'N': '-.',     'O': '---',
			'P': '.--.',   'Q': '--.-',   'R': '.-.',
			'S': '...',    'T': '-',      'U': '..-',
			'V': '...-',   'W': '.--',    'X': '-..-',
			'Y': '-.--',   'Z': '--..',	  ' ': '.......',
			'0': '-----',  '1': '.----',  '2': '..---',
			'3': '...--',  '4': '....-',  '5': '.....',
			'6': '-....',  '7': '--...',  '8': '---..',
			'9': '----.'}

	txt = txt.upper()
	morse_txt = ''
	for x in txt:
		morse_txt += codes[x] + ' '
	return morse_txt.strip()

def morse_to_audio(morse):
	for x in morse:
		print(x, end='')
		sys.stdout.flush()
		if x == '-':
			playsound('dash2.wav')
			time.sleep(DOT_TIME)
		elif x == '.':
			playsound('dot2.wav')
			time.sleep(DOT_TIME)
		elif x == ' ':
			time.sleep(3*DOT_TIME)
	print()

print("Enter some text to create Morse code audio:")
text = input()

while (all(x.isalnum() or x.isspace() for x in text) != True):
	print('Valid text is alphanumeric and spaces: ')
	text = input()

morse_text = morse(text)
print(morse_text)
morse_to_audio(morse_text)