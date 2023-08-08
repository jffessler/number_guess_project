#Random number class import
from randomNumber import randomNumber as rand
def number_generator():
    print("Welcome to the number guess game!")
    print("The mystery number is from 0 to infinity! Your choice!")
    while True:
        lower = int(input("Choose the lower bound: "))
        upper = int(input("Choose the upper bound: "))
        if lower < 0:
            print("Sorry, invalid input, lower bound must be greater than zero")
            continue
        elif upper < 0: 
            print("Sorry, invalid input, upper bound must be greater than zero")
            continue
        elif lower > upper:
            print("Sorry, invalid input, lower bound must be less than upper bound")
            continue
        else:
            break
    random_number = rand(lower,upper).random_number()
    return random_number,lower,upper
#Game logic
def num_guess(random_number,lower,upper):
    player_guess = -1
    # print(random_number)
    while True:
        player_guess = int(input(f"Guess the random number in the range of {lower} and {upper}: "))
        if abs(random_number - player_guess) > 10000:
            print("You are further than 10000 from the mystery number")
            continue
        elif abs(random_number - player_guess) > 1000:
            print("You are further than 1000 from the mystery number")
            continue
        elif abs(random_number - player_guess) > 100:
            print("You are further than 100 from the mystery number")
            continue
        elif abs(random_number - player_guess) > 25:
            print("You are further than 25 from the mystery number")
            continue
        elif abs(random_number - player_guess) > 10:
            print("You are further than 10 from the mystery number")
            continue
        elif abs(random_number - player_guess) < 10 and random_number != player_guess:
            print("You are within 10 from the mystery number")
            if random_number - player_guess < 0:
                print("Your number is too big!")
                continue
            elif random_number - player_guess > 0:
                print("Your number is too small!")
                continue
        elif random_number == player_guess:
            return print(f"Congratulations! You guessed the mystery number of {random_number}")
    
def play_Game():
    random_number, lower, upper = number_generator()
    num_guess(random_number,lower,upper)

play_Game()