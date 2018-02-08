import os.path #C:\\Users\\212407802\\Documents\\Edison\\University\\Computer Security\\Project1\\challenge1.txt
import math
import random

def main():
    toDecode = bytearray()
    nameIn = raw_input("Enter path of encrypted file: ")
    keyLength = 13
    with open(nameIn, "rb") as inFile:
        for line in inFile:
            for x in line:
                toDecode.append(x)
    zero=bytearray()
    one=bytearray()
    two=bytearray()
    three=bytearray()
    four=bytearray()
    five=bytearray()
    six=bytearray()
    seven=bytearray()
    eight=bytearray()
    nine=bytearray()
    ten=bytearray()
    eleven=bytearray()
    twelve=bytearray()
    for i in range(len(toDecode)):
        if i%keyLength == 0:
            zero.append(toDecode[i])
        if i%keyLength == 1:
            one.append(toDecode[i])
        if i%keyLength == 2:
            two.append(toDecode[i])
        if i%keyLength == 3:
            three.append(toDecode[i])
        if i%keyLength == 4:
            four.append(toDecode[i])
        if i%keyLength == 5:
            five.append(toDecode[i])
        if i%keyLength == 6:
            six.append(toDecode[i])
        if i%keyLength == 7:
            seven.append(toDecode[i])
        if i%keyLength == 8:
            eight.append(toDecode[i])
        if i%keyLength == 9:
            nine.append(toDecode[i])
        if i%keyLength == 10:
            ten.append(toDecode[i])
        if i%keyLength == 11:
            eleven.append(toDecode[i])
        if i%keyLength == 12:
            twelve.append(toDecode[i])
			

if __name__=="__main__":
    main()