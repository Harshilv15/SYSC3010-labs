import string
import random

secret = [random.choice('ABCDEF') for item in range (4)]

print("I've selected a 4-character secret code from the letters A,B,C,D,E and F.")
print ("I may have repeated some. ")
print ("Now, try and guess what I chose.")

yourguess = []

while list (yourguess) != secret:
    yourguess = input("Enter a 4-letter guess: eg ABCD : ").upper()
    if len(yourguess) != 4:
        continue
    
    
    print("you guessed ", yourguess)
    
    comparingList = zip(secret, yourguess)
    
    correctList = [speg for speg, gpeg in comparingList if speg == gpeg]
    
    fewestLetters = [min(secret.count(j), yourguess.count(j)) for j in 'ABCDEF']
    
    print("Number of correct letter is ", len(correctList))
    print("Number of unused letters is ", sum(fewestLetters) - len(correctList))
    
    print("YOU GOT THE ANSWER : ", secret)
    