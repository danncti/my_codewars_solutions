def decodeMorse(morse_code):
    MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

    morse_code = morse_code.replace('   ', ' x ')
    morse = morse_code.split()
    ret = []
    for m in morse:
        if m == 'x':
            ret.append(' ')
            continue
        ret.append(MORSE_CODE[m])
        print(m)
    return ''.join(ret).strip()

def decodeMorse2(morse_code):
    MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}
    print(MORSE_CODE)

    newlist = MORSE_CODE.items()
    sortedlist = sorted(newlist, key=lambda s: len(s[0]), reverse=True)
    ret = []
    while len(morse_code):

        for m, l in sortedlist:
            ml = len(m)
            print(m, l, ml)
            if m == morse_code[:ml]:
                print(m)
                ret.append(l)
                morse_code = morse_code[ml:]
                if morse_code[:3] == '   ':
                    ret.append(' ')
                    morse_code = morse_code[1:]
                morse_code = morse_code.strip()
                break
    return ''.join(ret)

import time

def main():

    tests = 1
    start_time = time.time()
    for a in range(tests):
        decodeMorse('.... . -.--   .--- ..- -.. .')

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
        main()