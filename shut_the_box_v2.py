# Shut the Box Game Code Version 2 (59 lines of Code)
# Version 2 allows the roll of single dice when the tiles available 
# are less than or equal to 6
# Fixed rollCheck function to check for addition four tile cases
# Lori Pfahler
# November 2024

import random

# variables
gameOver = False
availTiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rollOne = False
userInput = 'n'

# rollCheck function will check roll to see if it is feasible to continue play
# based on total from die and list of available numbers (i.e. availTiles in game code)
# Function will return "True" if roll has a least one playable solution;
# it will return "False" if not feasible.
#
# Note: This function is a brute force way to do this. This works since we need to 
# check only up to combinations of four numbers in this game. The smallest sum of five
# numbers would be 1+2+3+4+5 = 15 which is greater than the max roll of two die (12).
# This function was designed for a roll with 2 dice but works fine with only one.
#
# Using a recursive algorithm is the proper way to do this for more
# general situations. A recursion approach can be found via google

def rollCheck(rollTotal, availNums):
    # reduce availNums to all numbers <= dieTotal
    availNums = [x for x in availNums if x <= rollTotal]
    # create a variable for the length of availNums
    numsLen = len(availNums)
    # first check to see if a single number in availNums will work
    if rollTotal in availNums:
        return True
    # check sums of pairs of numbers in availNums if numsLen >= 2
    if numsLen >= 2: 
        for index1 in range(numsLen):
            for index2 in range(index1 + 1, numsLen):
                if sum([availNums[index1], availNums[index2]]) == rollTotal:
                    return True
    # check sums of three of numbers in availNums if numsLen >= 3
    if numsLen >= 3:
        for index1 in range(numsLen):
            for index2 in range(index1 + 1, numsLen):
                for index3 in range(index2 + 1, numsLen):
                    if sum([availNums[index1], availNums[index2],
                           availNums[index3]]) == rollTotal:
                        return True           
    # Only four combinations of four numbers is <= the max roll of 12
    # 1+2+3+4 = 10, 1+2+3+5 = 11, 1+2+3+6=12, and 1+2+4+5=12
    # check just these cases
    if rollTotal == 10 and all(x in availNums for x in [1, 2, 3, 4]):
        return True
    if rollTotal == 11 and all(x in availNums for x in [1, 2, 3, 5]):
        return True
    if rollTotal == 12 and all(x in availNums for x in [1, 2, 3, 6]):
        return True
    if rollTotal == 12 and all(x in availNums for x in [1, 2, 4, 5]):
        return True  
    # return False if none of the single numbers or possible sums from availNums will work 
    return False


# loop for game play
while gameOver == False:
    # check to see if one dice can be used
    if max(availTiles) <= 6:
        rollOne = True
    if rollOne:
        print('The tiles available:', availTiles)
        print('You may roll only one die since all available tiles are <= 6')
        userInput = input('Do you wish to roll one die only? (enter y or n) ').lower()
    # roll die/dice
    if userInput == 'y':
        die1 = random.randint(1,6)
        dieTotal = die1
        print('You roll:', die1)
    else:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        dieTotal = die1 + die2
        print('You roll:', die1, die2)
    print('The tiles available:', availTiles)
    # check to see if this roll has any possible solutions in availTiles
    if rollCheck(dieTotal, availTiles) == False:
        print('There is no play available for this roll.  Game over.')
        print('Your score:', sum(availTiles))
        gameOver = True
    # enter loop to check for user errors
    tileError = True
    while tileError == True and gameOver == False:
        # read in a list of the tiles to pull down from the player
        curChoices = [int(x) for x in input('Enter the tiles to pull down: ').split()]
        # check that the selection adds up correctly
        if sum(curChoices) != dieTotal:
            print('Your entry:', curChoices, 'does not equal the die total:', dieTotal)
            print('Try Again')
        # check that the selection is from tiles that are available
        elif (all(x in availTiles for x in curChoices) == False):
            print('Your entry includes tiles already used or numbers not in 1-9:', curChoices)
            print('Try Again') 
        else:
            # end user entry loop
            tileError = False
            # remove curChoices from availTiles
            for x in curChoices:
                availTiles.remove(x) 

    