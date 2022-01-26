# import random and time module
import random 
import time 

# create random range from 1-100 inclusive
n = random.randrange(1,100)

# welcome message
print ('hello, would you like to play the infamous GUESSING GAME OF GREATNESS?')
time.sleep(2)

# user input to enter number 
answer = int(input('what is your guess?'))

# game logic

while n != answer :
  # n is less than guess
  if answer < n : 
    print ('try again, too small ')
    answer = int(input('next guess: '))
  # n is less than guess
  elif answer > n:  
    print ('try again, too large ')
    answer = int(input('next guess: '))
  # else - stop if equal
  else :
    print('you won!') 
    break 
