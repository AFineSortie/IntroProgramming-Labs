mysteryAnimal = "snake"
quitVar = "q"

while True:
    print("\nI'm thinking of an animal...")
    guess = input("\nTake a guess what it is: ").lower()

    if guess == mysteryAnimal:
        print("\nThat's the one! Congratulations!")

        snakeLike = input("\nDo you like snakes y/n: ").lower()
        if snakeLike[0] == "y":
            print("\nAwww yea")

        elif snakeLike[0] == "n":
            print("\nGet out")

        else:
            print("\nThats not an answer I'm looking for!")
                
        break

    elif guess[0] == quitVar:
        print("You quitter!")
        break

    else:
        print("\nThat's not it... maybe you should try again?")


