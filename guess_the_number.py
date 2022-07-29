while True:
    import random

    secret_number = random.randint(1,100)

    print("Welcome to Guess the Number! You get 7 attempts to guess a number between 1 and 100, inclusive.")

    guess_count = 1

    while guess_count <= 7:
        guessed_number = input(f"This is guess number {guess_count} of 7. Guess the number: ")
        guessed_number = int(guessed_number)
        guess_count += 1
        if guessed_number == secret_number:
            print(f"That's right! The secret number was {secret_number}!")
            break
        elif guessed_number < secret_number:
            print(f"Not quite! The secret number is greater than {guessed_number}.")
        elif guessed_number > secret_number:
            print(f"Not quite! The secret number is less than {guessed_number}")

    again = input("Would you like to play again? Type \"Yes\" to play again or type \"No\" to exit. ")
    if again == "Yes":
        continue
    else:
        print("See you next time!")
        break