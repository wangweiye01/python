#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst nuber: ")
    if (first_number == 'q'):
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can not divide by 0!")
    else:
        print(answer)