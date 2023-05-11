import random

def mainRoll(rollInfo):
    # Checks if input is valid
    valid_letters = [0,1,2,3,4,5,6,7,8,9,"d","+", "-", " "]
    spaceSplit = rollInfo.split(' ')
    # item 1 of spaceSplit: Sides of dice & number of dice,
    # items 2+ of spaceSplit: multipliers and adders
    test1 = [i for ele in spaceSplit[0] for i in ele]
    for char in test1:
        if char.isnumeric() == False and char in valid_letters == False:
            #raise TypeError("Not a valid input!") #Not raising errors, because it would break a discord bot
            return('()That is not a valid input')

    # Sets up splits and items in lists
    try:
        d_split = spaceSplit[0].split("d")
        amount_of_dice = d_split[0]
        sidesOfDice = d_split[1]
    except IndexError: 
        amount_of_dice = 1
        sidesOfDice = spaceSplit[0]
    except:
        return('()An unknown error has occured')

    dice_rolls = []
    dice_add = None
    dice_multiply = None
    dice_sum = 0

    #Makes the number of dice work
    if amount_of_dice == "":
        amount_of_dice = 1
    else:
        amount_of_dice = int(amount_of_dice)

    #Returns an error if the sides on the dice isn't set
    if sidesOfDice == "":
        #raise TypeError("Not a valid input!")
        return('()That is not a valid input')
    else:
        sidesOfDice = int(sidesOfDice)

    # "Rolls" the dice
    for i in range(amount_of_dice):
        randomNumber = random.randint(1, sidesOfDice)
        dice_rolls.append(randomNumber)
        dice_sum += randomNumber

    # Runs operations
    if len(spaceSplit) > 1:
        # Arguments!
        for arg in spaceSplit[1:]:
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

    # Gives a "nice" looking output
    if len(dice_rolls) == 1 and dice_multiply == None and dice_add == None: return f'The random number is {dice_sum}'
    appendRoll = ''
    if dice_add != None: appendRoll += f'Added:{dice_add}; '
    if dice_multiply != None: appendRoll += f'Multiplied:{dice_multiply}; '
    if len(dice_rolls) == 1: appendRoll += f'Roll:{dice_rolls[0]}'
    if len(dice_rolls) >= 2: 
        rollsAppend = ''
        for i in range(0, len(dice_rolls)-1):
            rollsAppend += f'{dice_rolls[i]}, '
        rollsAppend += f'{dice_rolls[i+1]}'
        appendRoll += f'Rolls:{rollsAppend}'
    return f'The result is {dice_sum}\n{appendRoll}'