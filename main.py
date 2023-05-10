import roller

while True:
    try:
        print("What is your input:")
        rollValue = str(input())

        barkbarkkkAwrooo = roller.mainRoll(rollValue)
        if "()" in barkbarkkkAwrooo:
            woofbarkkkAwroooAWOOOO = barkbarkkkAwrooo[2:] #FYI!!! THIS IS THE EMIPHERIAL CODE FOR DISCORD BOTS!!!!
        else:
            woofbarkkkAwroooAWOOOO = barkbarkkkAwrooo
        print(woofbarkkkAwroooAWOOOO)

    except KeyboardInterrupt:
        exit("The program is closing...")