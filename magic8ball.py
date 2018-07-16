# https://bit.ly/2KZqTo8

import random

print("Welcome to Magic 8 Ball")
# print("What is your question?")
userInput = raw_input("What is your question?")

randomNumber = random.randint(1, 2)
if randomNumber == 1:
  print("Yes")
else:
  print("No")
