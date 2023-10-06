#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high!")
    return turns - 1
  elif guess < answer:
    print("Too low!")
    return turns - 1
  else:
    print("You win!")
    return

def set_difficulty():
  difficulty = input("Choose a difficulty level.'easy' or 'hard': ")
  if difficulty == "easy":
    return EASY_LEVEL_ATTEMPTS
  elif difficulty == "hard":
    return HARD_LEVEL_ATTEMPTS

def game():
  print(art.logo)
  print("Welcome to the game!")
  print("I'm thinking of a number between 1 to 100")

  answer = random.randint(1, 100)

  turns = set_difficulty()

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts reamining.")
    
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print(f"You loose! Answer was {answer}")
      return
game()
