#imports the random module
import random

#defines the function that will be used to generate a random word
with open('wordlist.txt', 'r') as f:
    wordlist = f.readlines()

#picks the random word from the list
word = random.choice(wordlist)[:-1]

#set the amount of failed guesses you can make
allowed_errors = 6
#tracks the guesses youve made
guesses = []
#controls the while loop
done = False

#prints the word with underscores for each letter that isnt guessed yet
while not done:
  for letter in word:
    if letter.lower() in guesses:
      print(letter, end=" ")
    else:
      print("_", end=" ")
  print("")
  done = True

  #Handles errors and the user guessses
  guess =  input(f"You have {allowed_errors} wrong guesses left, what's your next guess?")
  guesses.append(guess.lower())
  if guess.lower() not in word.lower():
    allowed_errors -= 1
    if allowed_errors == 0:
      break


  #Decides when the game is done
  done = True
  for letter in word:
      if letter.lower() not in guesses:
        done = False

#Fail message
if done:
  print(f"It was {word} !1!1!1!1!1!1!1!1")
else:
  print(f"You failed!!!!! It was {word}")