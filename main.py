import roller

while True:
    try:
        #Standard test code
        print("What is your input:")
        rollValue = str(input())

        #This is what happens when you let a furry choose variable names, lol
        # ^ okay i get that but these are just too long and look like eachother.
        # I recommend changing them.
        barkbarkkkAwrooo = roller.mainRoll(rollValue)
        if "()" in barkbarkkkAwrooo:
            woofbarkkkAwroooAWOOOO = barkbarkkkAwrooo[2:] #FYI!!! THIS IS THE EMIPHERIAL CODE FOR DISCORD BOTS!!!!
        else:
            woofbarkkkAwroooAWOOOO = barkbarkkkAwrooo
        print(woofbarkkkAwroooAWOOOO)

    except KeyboardInterrupt:
        exit("The program is closing...")