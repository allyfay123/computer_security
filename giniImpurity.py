import os.path #C:\\Users\\212407802\\Documents\\Edison\\University\\Computer Security\\Project1\\Project1\\challenge3.txt
import sys
import math

####################################################################
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ENGLISH_COMMON = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
####################################################################


def main():
    input = raw_input("Enter path of encrypted file: ")
    if (os.path.isfile(input)):
        input_file = open(input)
        file_txt = input_file.read()
        print("Encrypted text: \n\n" + file_txt)

        message_size = getMessageSize(file_txt)
        relFreq = getRelativeFreq(message_size, file_txt)
        gini = getGiniIndex(relFreq)
        print("The Gini Impurity Index is: ")
        print(gini)
        input_file.close()
                
    else:
        print("File does not exist.")

def getMessageSize(message):
    msgSize = 0
    for symbol in message.upper():
        if symbol in ALPHABET:
            msgSize += 1
    return msgSize

def getLetterCount(message):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
                   'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0,
                   'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                   'Y': 0, 'Z': 0}
    
    for symbol in message.upper():
        if symbol in ALPHABET:
            letterCount[symbol] += 1
    return letterCount


def getRelativeFreq(messageSize, file):
    relativeFreq = {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0, 'F': 0.0, 'G': 0.0, 'H': 0.0,
                   'I': 0.0, 'J': 0.0, 'K': 0.0, 'L': 0.0, 'M': 0.0, 'N': 0.0, 'O': 0.0, 'P': 0.0,
                   'Q': 0.0, 'R': 0.0, 'S': 0.0, 'T': 0.0, 'U': 0.0, 'V': 0.0, 'W': 0.0, 'X': 0.0,
                   'Y': 0.0, 'Z': 0.0}
    letter_count = getLetterCount(file)
    for symbol in ALPHABET:
        relativeFreq[symbol] = letter_count[symbol]/float(messageSize)
    return relativeFreq

def getGiniIndex(relative_freq):
    sum = 0
    for symbol in ALPHABET:
        sum += relative_freq[symbol] * relative_freq[symbol]
    giniIndex = 1-sum
    return giniIndex

if __name__=="__main__":
    main()