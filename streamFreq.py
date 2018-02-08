import os.path #C:\\Users\\212407802\\Documents\\Edison\\University\\Computer Security\\Project1\\challenge1.txt
import math
import random
from collections import Counter

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

    cnt0 = Counter()
    for value in zero:
	    cnt0[value] +=1
    print cnt0

    cnt1 = Counter()
    for value in one:
	    cnt1[value] +=1
    print cnt1
	
    cnt2 = Counter()
    for value in two:
	    cnt2[value] +=1
    print cnt2
	
    cnt3 = Counter()
    for value in three:
	    cnt3[value] +=1
    print cnt3

    cnt4 = Counter()
    for value in four:
	    cnt4[value] +=1
    print cnt4

    cnt5 = Counter()
    for value in five:
	    cnt5[value] +=1
    print cnt5

    cnt6 = Counter()
    for value in six:
	    cnt6[value] +=1
    print cnt6
	
    cnt7 = Counter()
    for value in seven:
	    cnt7[value] +=1
    print cnt7
	
    cnt8 = Counter()
    for value in eight:
	    cnt8[value] +=1
    print cnt8

    cnt9 = Counter()
    for value in nine:
	    cnt9[value] +=1
    print cnt9

    cnt10 = Counter()
    for value in ten:
	    cnt10[value] +=1
    print cnt10
	
    cnt11 = Counter()
    for value in eleven:
	    cnt11[value] +=1
    print cnt11

    cnt12 = Counter()
    for value in twelve:
	    cnt12[value] +=1
    print cnt12
	
if __name__=="__main__":
    main()