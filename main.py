import roller

while True:
    try:
        #Standard test code
        print("What is your input:")
        rollValue = str(input())

        roller.mainRoll(rollValue)

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
        # print("The Program is terminated manually!")
        # raise SystemExit # Dont do this
        # Do this instead
        exit("The Program is terminated manually!") # this prints the message and exits