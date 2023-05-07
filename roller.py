import random

def repeatedContains(checkValue, checkList):
    if contains(checkValue, checkList) == True:
        index = 0
        positionsList = []
        while index < len(checkValue):
            index = checkValue.find(checkList, index)
            if index == -1: break
            #print('ll found at', index)
            index += len(checkList)
            positionsList.append(index)
        ##write the code here to tell if it will work as it should
        if len(positionsList) == 1: return positionsList[0]
        if len(positionsList) == 2: return 2
        else: return True
    return False

# This function is useless as it can be combined to one line like so
# (you can just use this right in the code without needing a function):
# somevarname = [i for i in checkValue if i in checkList] != [] # Boolean
# if somevarname == True: do stuff

# What the `[i for i in checkValue if i in checkList]` does is it loops
# through each element in checkValue and checks if it is in checkList and
# if it is, it adds it to a list. If the list is not empty, it returns True.

# IF YOU REALLY WANT TO KEEP THIS A FUNCTION:
# There is a much better way to do this if you really want to do it like this:

def contains(checkValue, checkList):
    for element in checkValue: # Loops through each element in checkValue
       if element in checkList: return True # If the element is in checkList, return True
    return False # If the loop ends, return False

# Or if you want a one-liner you can do this:
# somevarname = [i for i in checkValue if i not in checkList] != [] # Boolean
# if somevarname == True: do stuff

def validInput(checkValue, checkList):
    for element in range(0, len(checkValue)):
        # Instead change to this:
        # if checkValue[element] not in checkList: return False
        if checkValue[element] in checkList: pass # Remove this
        else: return False # Remove this
    return True


def numberStringer(listOfNumbers):
    if len(listOfNumbers) == 2: return f'{listOfNumbers[0]} and {listOfNumbers[1]}'
    barkAwoo = "" #Why that name? ... don't ask ~~It may or may not be because I am a furry. who would have guessed~~
    for element in range(0, len(listOfNumbers)-1): # no error here but 
        # why do you name it element if its not the element? its a bit confusing
        barkAwoo.append(f'{element}, ')
    barkAwoo.append(f'and {listOfNumbers[len(listOfNumbers)]}')
    return barkAwoo
        
# I'm assuming that this is not finished
def postWork(number, parts, multiply = None, add = None):
    # Make it a list PAW!!!!!!!!!
    if len(parts) == 1 and multiply == None and add == None: return f'The random number is {number}'
    if len(parts) == 1 and multiply == None and add != None: return f'The random number is {number+add}.\nWhich accounts for an added {add}, and the original number was {number}'
    
    if len(parts) == 1 and multiply == None and add == None: return f'The random number is {number}'
    if len(parts) == 1 and multiply == None and add != None: return f'The random number is {number+add}.\nWhich accounts for an added {add}, and the original number was {number}'
    barkkbarkkk = numberStringer(parts)
    if len(parts) != 1 and add == None: return f'The random number is {number}.\nIt is made up of the rolls: {barkkbarkkk}'
    if len(parts) != 1 and add != None: return f'The random number is {number+add}.\nWhich accounts for an added {add}, and the original number was {number}'

def mainRoll(rollInfo):
    valid_letters = [0,1,2,3,4,5,6,7,8,9,"d","+", "-", " "]
    spootSplit = rollInfo.split()
    # item 1 of spootSplit: Sides of dice & number of dice,
    # items 2+ of spootSplit: multipliers and adders

    # This piece of code will loop through the first argument and check if it is
    # a valid input then add it to a list. If it is not a valid input, it will
    # raise a TypeError. #Not anymore :3
    firstargs = []
    for char in spootSplit[0].split():
        print("Trying: "+char)
        if char.isnumeric():
            # Valid!
            firstargs.append(int(char))
            print(char+" is numerically valid")
        elif char in valid_letters:
            # Valid!
            firstargs.append(char)
            print(char+" is on the letters list valid")
        else:
            # Not valid!
            #raise TypeError("Not a valid input!") #Not raising errors, because it would break a discord bot
            return('()That is not a valid input')

    d_split = spootSplit[0].split("d")
    amount_of_dice = d_split[0]
    sidesOfDice = d_split[1]
    dice_rolls = [] # for if you have to return each
    dice_add = None
    dice_sum = 0 # for if you have to return the total sum

    if amount_of_dice == "":
        amount_of_dice = 1
    else:
        amount_of_dice = int(amount_of_dice)

    if sidesOfDice == "":
        #raise TypeError("Not a valid input!")
        return('()That is not a valid input')

    else:
        sidesOfDice = int(sidesOfDice)

    # # IF YOU HAVE TO RETURN EACH SUM OF DICE:
    # for i in range(amount_of_dice):
    #     dice_rolls.append(random.randint(1, sidesOfDice))

    # # IF YOU HAVE TO RETURN THE TOTAL SUM OF DICE:
    # for i in range(amount_of_dice):
    #     dice_sum += random.randint(1, sidesOfDice)

    #This should work for both of the above things together (without the issue of different ints)
    for i in range(amount_of_dice):
        AWOOOOO = random.randint(1, sidesOfDice)
        dice_rolls.append(AWOOOOO)
        dice_sum += AWOOOOO

    if len(spootSplit) > 1:
        # Arguments!
        for arg in spootSplit[1:]:
            if arg.startswith("+"):
                # Add
                dice_sum += int(arg[1:])
                dice_add = int(arg[1:])
            if arg.startswith("-"):
                # Subtract
                dice_sum -= int(arg[1:])
                dice_add = int(arg[1:])

    return postWork(dice_sum, dice_rolls, dice_add)

    # except:
    #     return("An error has occured! Please try again! (check and make sure you do not have too many arguements)")