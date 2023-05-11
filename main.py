import roller

while True:
    try:
        print("What is your input:")
        rollValue = str(input())

        rollOutput = roller.mainRoll(rollValue)
        if "()" in rollOutput:
            finalOutput = rollOutput[2:] #FYI!!! THIS IS THE EMIPHERIAL CODE FOR DISCORD BOTS!!!!
        else:
            finalOutput = rollOutput
        print(finalOutput)

    except KeyboardInterrupt:
        exit("The program is closing...")