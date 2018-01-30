#with open(raw_input(), 'rU') as input_file:
#    input("File to decode: ")

#print("" + input_file)

#print("hello")

import os.path #C:\\Users\\schmi\\Documents\\Computer Security\\Project1\\Project1\\challenge3.txt
import sys
import math

input = raw_input("Enter path of encrypted file: ")
if (os.path.isfile(input)):
        #print("Opening and reading file...")
    #input_file = open(input)
    #file_txt = input_file.read()
    #input_file.close()
    #print("Encrypted text: \n\n" + file_txt)

    f = open(input, "rb")
    bytes = map(ord, f.read())

    f.close()
    file_size = len(bytes)
    print ("File size (bytes): " + str(file_size))

    #calculate frequiency of each byte
    frequencies = []
    for b in range(256):
        ctr = 0
        for byte in bytes:
            if byte == b:
                ctr += 1
                frequencies.append(float(ctr)/file_size)

    print(frequencies)
    print("hello")
                
else:
    print("File does not exist.")

