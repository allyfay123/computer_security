import os.path #C:\\Users\\212407802\\Documents\\Edison\\University\\Computer Security\\Project1\\challenge1.txt
import math
import random

def main():
    toDecode = bytearray()
    nameIn = raw_input("Enter path of encrypted file: ")
    with open(nameIn, "rb") as inFile:
        for line in inFile:
            for x in line:
                toDecode.append(x)
    #print(toDecode)
    sum = 0	
    for i in range(len(toDecode)):
        if toDecode[i] == toDecode[i+4]
            sum += 1
    print("coincidents for x=4 is " + sum)


if __name__=="__main__":
    main()