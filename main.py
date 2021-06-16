#Number Guessing Game Objectives:
import random

# Include an ASCII art logo.
logo = """" _____                       _   _                                  _               
|  __ \                     | | | |                                | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                    
                                                                                    
"""
print(logo)
print("Welcome to the number guessing name")
print("I'm thinking of a number between 1 and 100. ")

guess_the_number = random.randint(1,100)
print(f"believe or not the correct answer is {guess_the_number}")

attempts_hard = 5
attempts_easy = 10

def difficulty(difficulty):
  if difficulty == "hard":
    global attempts_hard
    while attempts_hard != 0:
      print(f"You have {attempts_hard} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      attempts_hard -= 1
      if guess == guess_the_number:
        print(f"You got it! The answer was {guess_the_number}")
      elif attempts_hard == 0:
        print("You 've run out of guesses. You lose")
      elif guess > guess_the_number:
        print("Too high")
      elif guess < guess_the_number:
        print("Too low")
  elif difficulty == "easy":
    global attempts_easy
    while attempts_easy != 0:
      print(f"You have {attempts_hard} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      attempts_hard -= 1
      if guess == guess_the_number:
        print(f"You got it! The answer was {guess_the_number}")
      elif attempts_hard == 0:
        print("You 've run out of guesses. You lose")
      elif guess > guess_the_number:
        print("Too high")
      elif guess < guess_the_number:
        print("Too low")
      
      
difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))







# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

