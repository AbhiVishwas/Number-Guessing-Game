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
count = 1 
while n != answer and count < 5 :
  # n is less than guess and if count is under 5 
  if answer < n : 
    print ('try again, too small ')
    print ('You have {} attempts left'.format((5-count)))
    answer = int(input('next guess: '))
    count += 1
  # n is less than guess
  elif answer > n:  
    print ('try again, too large ')
    print ('You have {} attempts left'.format((5-count)))
    answer = int(input('next guess: '))
    count += 1
  # else - stop if equal
  else :
    break 

if answer == n:   
  print('you won!') 
else: 
    print ('bad luck!')
