# create rock scissors paper program that asks for user input
# 0 = rock 1 = scissors 2 = paper

import random

def whatIsIt(num):
  if num < 0 or num > 2: 
    return "You gave a wrong number! Number has to be between 0 and 2"
  choices = ["Rock", "Scissors", "Paper"]
  return choices[num]

#gives back 0-2 at random
def computerChoice():
  return random.randint(0, 2)

def rockScissorsPaper():
  #Code Here

  #print random computer response
  print(whatIsIt(computerChoice()))

rockScissorsPaper()
#code here
#ask user for a choice of rock  scissor paper 
user_choice =input("choose rock or scissors or paper: ")
print(user_choice)

#if statement that checks if user's choice is correct 
if: choice == "rock" or choice == "scissors" or 
choice == "paper":
print("your response is not valid")

#print tie if user and computer response is the same 
computer_choice = whatIsIt(computerChoice())
print("computer_choice: ")
print(computer_choice)

#print tie if random computer response is the same 
if user_choice == computer_choice: 
  print("it's a tie ")
else:
  print("it's not a tie")
else:
if user_choice == "rock"  
   if computer_choice == "scissors":
     print("the user won!")
if computer_choice == "paper"
     print("the computer won!")
elif user_choice == "scissors":
  




