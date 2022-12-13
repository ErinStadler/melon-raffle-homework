"""A number-guessing game."""

# Put your code here
# Used the source quoted for finding the random function -- https://thecleverprogrammer.com/2022/06/29/number-guessing-game-using-python/#:~:text=So%20below%20is%20how%20you,%3A%20print(%22Too%20high!
def guessing_game():

    import random #imports random function

    name = input("What is your name?")
    print(name + ", I'm thinking of a number between 1 and 100.")
    print("Try to guess my number.")

    secret_guess = random.randint(1 , 100)
    players_guess = int(input("Your guess?"))
    print(players_guess)

    too_low = 0
    too_high = 101
    number_of_tries = 0

    while secret_guess != players_guess:

        if secret_guess > players_guess:
            print("Too low, please guess again.")
            players_guess = int(input("Your guess?"))
            number_of_tries = number_of_tries + 1
        else:
            print("Too high, please guess again.")
            players_guess = int(input("Your guess?"))
            number_of_tries = number_of_tries + 1

    print(f"Well done, {name}! You found my number in {number_of_tries} tries!")

guessing_game()