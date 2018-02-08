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
    fourToTwenty = range(4,40)
    print(len(toDecode))
    for value in fourToTwenty:
        for i in range(len(toDecode)-value):
            if toDecode[i] == toDecode[i+value]:
                sum += 1
        print("coincidence for ", value, "is ", sum)
        sum=0


if __name__=="__main__":
    main()