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

# def contains(checkValue, checkList):
#     for element in checkValue: # Loops through each element in checkValue
#        if element in checkList: return True # If the element is in checkList, return True
#    return False # If the loop ends, return False
def contains(checkValue, checkList):
    for element in range(0, len(checkValue)):
        #print(checkValue[element])
        if checkValue[element] in checkList: return True
    return False


# For this don't use pass in that if statment, just do an "if not" statement
# like so:

# def validInput(checkValue, checkList):
#    for element in checkValue:
#        if element not in checkList: return False
#    return True

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
    barkAwoo = ""
    for element in range(0, len(listOfNumbers)-1): # no error here but 
        # why do you name it element if its not the element? its a bit confusing
        barkAwoo.append(f'{element}, and ')
    barkAwoo.append(listOfNumbers[len(listOfNumbers)])
    return barkAwoo
        
# I'm assuming that this is not finished
def postWork(number, multiplier = None, add = None):
    # Make it a list PAW!!!!!!!!!
    if len(number) == 1 and multiplier == None and add == None: return f'The random number is {number}'
    if len(number) == 1 and multiplier == None and add != None: return f'The random number is {number+add}.\nWhich accounts for an added {add}, and the original number was {number}'
    barkkbarkkk = numberStringer(number)

    pass



def mainRoll(rollInfo):
    valid_letters = ['d',]
    #usedCharacters = [0,1,2,3,4,5,6,7,8,9,"d","*","+", "-", " "]
    #if validInput(rollInfo, usedCharacters) == False: return "ERROR: NOT A VALID INPUT"
    spootSplit = rollInfo.split(" ")
    # item 1 of spootSplit: Sides of dice & number of dice,
    # items 2+ of spootSplit: multipliers and adders
    print(spootSplit)

    # This piece of code will loop through the first argument and check if it is
    # a valid input then add it to a list. If it is not a valid input, it will
    # raise a TypeError.
    firstargs = []
    for char in spootSplit[0].split(""):
        if char.isnumeric():
            # Valid!
            firstargs.append(int(char))
        elif char in valid_letters:
            # Valid!
            firstargs.append(char)
        else:
            # Not valid!
            raise TypeError("Not a valid input!")

    d_split = spootSplit[0].split("d")
    amount_of_dice = d_split[0]
    sides_of_dice = d_split[1]
    dice_rolls = [] # for if you have to return each
    dice_sum = 0 # for if you have to return the total sum

    if amount_of_dice == "":
        amount_of_dice = 1
    else:
        amount_of_dice = int(amount_of_dice)

    if sides_of_dice == "":
        raise TypeError("Not a valid input!")

    else:
        sides_of_dice = int(sides_of_dice)

    # IF YOU HAVE TO RETURN EACH SUM OF DICE:
    # for i in range(amount_of_dice):
        # dice_rolls.append(random.randint(1, sides_of_dice))

    # IF YOU HAVE TO RETURN THE TOTAL SUM OF DICE:
    for i in range(amount_of_dice):
        dice_sum += random.randint(1, sides_of_dice)

    if len(spootSplit) > 1:
        # Arguments!
        for arg in spootSplit[1:]:
            if arg.startswith("+"):
                # Add
                dice_sum += int(arg[1:])

    return dice_sum
    


    # try:
    #     if rollInfo.isnumeric() == True: return postWork(random.randint(rollInfo, 1))
    #     if contains(rollInfo, "d") == True:
    #         pass #arguemtns for the actuall rolling. seperated by a ";"
    #     if contains(rollInfo, "*") == True:
    #         pass #protocol for the multiplication
    # except TypeError:
    #     return "ERROR: NOT A VALID INPUT"
    # except:
    #     return("An error has occured! Please try again! (check and make sure you do not have too many arguements)")