import random

# def numberStringer(listOfNumbers, method):
#     barkAwoo = None
#     if method == 1:
#         if len(listOfNumbers) == 2: return f'{listOfNumbers[0]} and {listOfNumbers[1]}'
#         barkAwoo = "" #Why that name? ... don't ask
#         for element in range(0, len(listOfNumbers)-1):
#             barkAwoo += f'{element}, '
#         barkAwoo += f'and {listOfNumbers[-1]}' # The index is out of range here, list counts start at 0, so you have to subtract one like you did above
#         # ^^^ -1 is the last item of the list
#         return barkAwoo
#     if method == 2:
#         for element in range(0, len(listOfNumbers)-1): barkAwoo += f'{element}; '
#         barkAwoo += f'{element}'

def postWork(number, parts, multiply = None, add = None):
    # just do stuff like `if not multiply` or something to make it shorter
    if len(parts) == 1 and multiply == None and add == None: return f'The random number is {number}'
    barkAppend = ''
    if add != None: barkAppend += f'Added:{add}; '
    if multiply != None: barkAppend += f'Multiplied:{multiply}; '
    if len(parts) == 1: barkAppend += f'Roll:{parts[0]}'
    if len(parts) >= 2: 
        barkAwoo = ''
        for element in range(0, len(parts)-1): barkAwoo += f'{element}; '
        barkAwoo += f'{element}'
        barkAppend += f'Rolls:{barkAwoo}'
    return f'The result is {number}\n{barkAppend}'

    # # Old code to remove
    # if len(parts) == 1 and multiply == None and add != None: return f'The random number is {number+add}.\nAdded:{add}; Original Roll:{number};'
    
    # if len(parts) == 1 and multiply == None and add == None: return f'The random number is {number}'
    # if len(parts) == 1 and multiply == None and add != None: return f'The random number is {number+add}.\nAdded:{add}; and the original number is {number};'
    # barkkbarkkk = numberStringer(parts, 1)
    # if len(parts) != 1 and multiply == None and add == None: return f'The random number is {number}.\nRolls:{barkkbarkkk};'
    # if len(parts) != 1 and multiply == None and add != None: return f'The random number is {number+add}.\nAdded:{add}; Rolls:{barkkbarkkk};'

    # if len(parts) != 1 and multiply != None and add == None: return f''
    # if len(parts) != 1 and multiply != None and add != None: return f''

def mainRoll(rollInfo):
    valid_letters = [0,1,2,3,4,5,6,7,8,9,"d","+", "-", " "]
    spootSplit = rollInfo.split(" ")
    # item 1 of spootSplit: Sides of dice & number of dice,
    # items 2+ of spootSplit: multipliers and adders

    # This piece of code will loop through the first argument and check if it is
    # a valid input then add it to a list. If it is not a valid input, it will
    # raise a TypeError. #Not anymore :3
    firstargs = []
    # for char in spootSplit[0].split():
    test1 = [i for ele in spootSplit[0] for i in ele]
    for char in test1:# spootSplit[0].split():
        # print("Trying: "+char)
        if char.isnumeric():
            # Valid!
            firstargs.append(int(char))
        elif char in valid_letters:
            # Valid!
            firstargs.append(char)
        else:
            print(char)
            # Not valid!
            #raise TypeError("Not a valid input!") #Not raising errors, because it would break a discord bot
            return('()That is not a valid input')

    d_split = spootSplit[0].split("d")
    amount_of_dice = d_split[0]
    sidesOfDice = d_split[1]
    dice_rolls = []
    dice_add = None
    dice_multiply = None
    dice_sum = 0

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
        awooooo = random.randint(1, sidesOfDice)
        dice_rolls.append(awooooo)
        dice_sum += awooooo

    if len(spootSplit) > 1:
        # Arguments!
        for arg in spootSplit[1:]:
            if arg.startswith("+"):
                # Add
                dice_sum += int(arg[1:])
                dice_add = int(arg[1:])
            if arg.startswith("-"):
                # Subtract
                if dice_add != None: return('()You can\'t have a plus and minus operation at the same time.')
                dice_sum -= int(arg[1:])
                dice_add = int(arg[1:])
            if arg.startswith("*"):
                # Multiply
                dice_sum = int(dice_sum)*int(arg[1:])
                dice_multiply = int(arg[1:])

    return postWork(dice_sum, dice_rolls, dice_multiply, dice_add)