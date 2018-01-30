import os.path #C:\\Users\\schmi\\Documents\\Computer Security\\Project1\\Project1\\challenge3.txt
import sys
import math

################################################################
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ENGLISH_COMMON = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
################################################################


def main():
    input = raw_input("Enter path of encrypted file: ")
    if (os.path.isfile(input)):
        input_file = open(input)
        file_txt = input_file.read()
        print("Encrypted text: \n\n" + file_txt)

        letter_count = getLetterCount(file_txt)
        print("The number of occurrences of each symbol in the "
              + "alphabet is as follows:")
        print(letter_count)
        print
        frequencies = getFreqInOrder(file_txt)
        print("The order of symbols in terms of highest frequency "
              + "is as follows:")
        print(frequencies)
        input_file.close()
                
    else:
        print("File does not exist.")

def getLetterCount(message):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
                   'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0,
                   'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                   'Y': 0, 'Z': 0}
    
    for symbol in message.upper():
        if symbol in ALPHABET:
            letterCount[symbol] += 1
    return letterCount

def getFreqInOrder(message):
    letterToFreq = getLetterCount(message)
    freqToLetter = {}
    for symbol in ALPHABET:
        if letterToFreq[symbol] not in freqToLetter:
            freqToLetter[letterToFreq[symbol]] = [symbol]
        else:
            freqToLetter[letterToFreq[symbol]].append(symbol)

    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ENGLISH_COMMON.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)

def getItemAtIndexZero(x):
    return x[0]

if __name__=="__main__":
    main()
