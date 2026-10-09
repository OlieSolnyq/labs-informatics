#!/usr/bin/python3
word = input()
if word == word[::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
