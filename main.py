import roller

while True:
    try:
        #Standard test code
        print("What is your input:")
        rollValue = str(input())

        #This is what happens when you let a furry choose variable names, lol
        barkbarkkkAwrooo = roller.mainRoll(rollValue)
        if barkbarkkkAwrooo[0:2] == "()":
            woofbarkkkAwroooAWOOOO = barkbarkkkAwrooo[2:] #FYI!!! THIS IS THE EMIPHERIAL CODE FOR DISCORD BOTS!!!!
        else:
            woofbarkkkAwroooAWOOOO = barkbarkkkAwrooo
        print(woofbarkkkAwroooAWOOOO)

        # Testing Repeated Contains Function
        # print("What are you looking for:")
        # secondInput = str(input())
        # print(f'The string \"{rollValue}\" has \"{secondInput}\" returns: {roller.repeatedContains(rollValue, secondInput)}')

        # Testing Contains Function
        # print("What are you looking for:")
        # secondInput = str(input())
        # print(f'The string \"{rollValue}\" has \"{secondInput}\" returns: {roller.contains(rollValue, secondInput)}')

        # The following lines are test of the valid Input thing
        # usedCharacters = ['0','1','2','3','4','5','6','7','8','9','d','*','+', '-', ' ']
        # print(f'The result of \"{rollValue}\" running the check is: {roller.validInput(rollValue, usedCharacters)}')

    except KeyboardInterrupt:
        exit("The program is closing...")