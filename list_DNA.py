#!/usr/bin/python3
import random
randomseq = ''
nucl = ["A", "T","G","C"]
for i in range(10):
    randomseq += random.choice(nucl)
print(randomseq)
givenseq = str(input())
for x in givenseq:
    if x != "A" and x != "T" and x != "G" and x != "C":
        print("This is not a DNA sequence")
        break
print("A count:" + str(givenseq.count("A")))
print("T count:" + str(givenseq.count("T")))
print("G count:" + str(givenseq.count("G")))
print("C count:" + str(givenseq.count("C")))

compseq = ""
for x in givenseq:
    if x == "A":
        compseq += 'T'
    if x == "T":
        compseq += 'A'
    if x == "G":
        compseq += 'C'
    if x == "C":
        compseq += 'G'
print(compseq)



