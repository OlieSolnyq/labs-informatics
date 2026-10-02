#!/usr/bin/python3
import random
randomseq = ''
nucl = ["A", "T","G","C"]
#print("Insert the length of the DNA:")
length = int(input())
for i in range(length):
    randomseq += random.choice(nucl)
print(randomseq)


