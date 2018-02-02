import os.path #C:\\Users\\schmi\\Documents\\Computer Security\\Project1\\Project1\\challenge3.txt
import sys
import math
import collections

####################################################################
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ENGLISH_COMMON = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
ENGLISH_COMMON_FREQUENCY = englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17,
 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 
 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 
 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 
 'Q': 0.10, 'Z': 0.07}
####################################################################


def main():
    input = raw_input("Enter path of encrypted file: ")
    if (os.path.isfile(input)):
        input_file = open(input)
        file_txt = input_file.read()
        print("Encrypted text: \n\n" + file_txt)

        ioc = getIndexOfCoincidence(file_txt)
        print("The index of coincidence is as follows:")
        print(ioc)
        input_file.close()
                
    else:
        print("File does not exist.")

def getIndexOfCoincidence(message):
    n = len(message)
    frequencies = collections.Counter(message)
    sum = 0.0
    
    for symbol in ALPHABET:
        sum += frequencies[symbol] * (frequencies[symbol]-1)
        
    ioc = sum/(n*(n-1))
    
    return ioc

def getKeyLen(message, ioc):
    n = len(message)
    k = (0.0265 * n) / ((0.065 - ioc) + n * (ioc - 0.0385))
    return k

if __name__=="__main__":
    main()
