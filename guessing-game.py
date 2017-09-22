mysteryAnimal = "snake"

while True:
    print("\nI'm thinking of an animal...")
    guess = input("\nTake a guess what it is: ").lower()
    if guess == mysteryAnimal:
        break
    elif guess == "quit":
        break
    else:
        print("\nThat's not it... maybe you should try again?")

print("\nThat's the one! Congratulations!")
