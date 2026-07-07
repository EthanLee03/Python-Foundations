import random 


def main():
    number = random.randint(1,10)
    turns = 0 

    while True:
        user_guess = int(input("What number are you guessing? "))
        turns += 1
        if user_guess == number:
            print("You guessed the number correctly!")
            print (" You took this many turns", turns)
        else:
            print("You guessed wrong")

        if user_guess > number:
            print("Lower!")
        elif user_guess < number: 
            print("Higher!")

        if user_guess == number:
            break


            
        
    
    



main()