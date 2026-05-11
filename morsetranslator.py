# Morse Code Translator by ZackFairTheOne
# Translates your text to Morse Code, duh! Feel free to enhance since im dumb as fuck.
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',
    'X': '-..-',  'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    ' ': '/'
}

def text_to_morse(text):
    morse = []

    for char in text.upper():
        if char in MORSE_CODE:
            morse.append(MORSE_CODE[char])
        else:
            morse.append('?')

    return ' '.join(morse)

# Why do i suck at coding?
text = "Your Friendly Text here"

print("Original:", text)
print("Morse:", text_to_morse(text))