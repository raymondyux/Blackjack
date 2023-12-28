import os
from art import logo
import random

def clear():
  os.system('clear')

#Compute score of cards
def score(list_of_cards):
  if len(list_of_cards) == 2 and sum(list_of_cards) == 21:
    return 0
  if 11 in list_of_cards and sum(list_of_cards) > 21:
    list_of_cards.remove(11)
    list_of_cards.append(1)
  
  return sum(list_of_cards)

def new_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def compare(my_score, computer_score):
  if computer_score == my_score:
    return "It's a draw. No win no lose."
  elif computer_score == 0 :
    return "Opponent has blackjack. You lose!"
  elif my_score == 0:
    return "You have blackjack. You win!"
  elif my_score > 21:
    return "You went over. You lose!"
  elif computer_score > 21:
    return "Opponent went over. You win!"
  elif my_score > computer_score:
    return "You win!"
  else:
    return "You lose!"

def game():
  print(logo)
  my_cards = []
  computer_cards = []
  game_is_over = False
  
  for _ in range(2):
    my_cards.append(new_card())
    computer_cards.append(new_card())
  
  while not game_is_over:
    my_score = score(my_cards)
    computer_score = score(computer_cards)
    print(f"  Your final hand: {my_cards}, final score: {my_score}")
    print(f"  Computer's first card: {computer_cards[0]}")
    if score(my_cards) == 0 or score(computer_cards) == 0 or score(my_cards) > 21:
      game_is_over = True
    else:
      continue_option = input("Tyep 'y' to get another cards, type 'n' to pass: ")
      if continue_option == 'y':
          #my_cards do not exceed 21
          my_cards.append(new_card())
      else:
        game_is_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(new_card())
    computer_score = score(computer_cards)
  
  print(f"Your final hand: {my_cards}, final score: {my_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(my_score, computer_score))
  

while input("Do you want to play a game of Blackkjack. Type 'y' or 'n': ") == 'y':
  #clear the previous screen
  clear()
  game()