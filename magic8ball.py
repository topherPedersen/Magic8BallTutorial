# https://bit.ly/2KZqTo8

import random

print("Welcome to Magic 8 Ball")

fortune = []
fortune.append("It is certain.")
fortune.append("It is decidedly so.")
fortune.append("Without a doubt.")
fortune.append("Yes, definitely.")
fortune.append("You may rely on it.")
fortune.append("As I see it, yes.")
fortune.append("Most likely.")
fortune.append("Outlook good.")
fortune.append("Yes.")
fortune.append("Signs point to yes.")
fortune.append("Reply hazy, try again.")
fortune.append("Ask again later.")
fortune.append("Better not tell you now.")
fortune.append("Cannot predict now.")
fortune.append("Concentrate and ask again.")
fortune.append("Don't count on it.")
fortune.append("My reply is no.")
fortune.append("My sources say no.")
fortune.append("Outlook not so good.")
fortune.append("Very doubtful.")

# Extra credit if you can spot the easy way
# to do this without using an if-statement :)

keepPlaying = True
while keepPlaying == True:
  
  userInput = raw_input("What is your question?")
  
  randomNumber = random.randint(0, 19)
  
  if randomNumber == 0:
    print(fortune[0])
  elif randomNumber == 1:
    print(fortune[1])
  elif randomNumber == 2:
    print(fortune[2])
  elif randomNumber == 3:
    print(fortune[3])
  elif randomNumber == 4:
    print(fortune[4])
  elif randomNumber == 5:
    print(fortune[5])
  elif randomNumber == 6:
    print(fortune[6])
  elif randomNumber == 7:
    print(fortune[7])
  elif randomNumber == 8:
    print(fortune[8])
  elif randomNumber == 9:
    print(fortune[9])
  elif randomNumber == 10:
    print(fortune[10])
  elif randomNumber == 11:
    print(fortune[11])
  elif randomNumber == 12:
    print(fortune[12])
  elif randomNumber == 13:
    print(fortune[13])
  elif randomNumber == 14:
    print(fortune[14])
  elif randomNumber == 15:
    print(fortune[15])
  elif randomNumber == 16:
    print(fortune[16])
  elif randomNumber == 17:
    print(fortune[17])
  elif randomNumber == 18:
    print(fortune[18])
  elif randomNumber == 19:
    print(fortune[19])
    
  userResponse = raw_input("Would you like to continue playing? (answer 'y' for yes, 'n' for no)")
  if userResponse == "y":
    keepPlaying = True
  else:
    keepPlaying = False
    print("Goodbye!")
