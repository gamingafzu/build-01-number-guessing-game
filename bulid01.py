import random

while True:
    secret_number = random.randint(1, 100)
    #print(secret_number)
    attempts = 0
    guess = None

    while guess != secret_number:
        try:
            guess = int(input("guess a number between 1 and 100:"))
        except ValueError:
            print("please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("1 se 100 ke bichh main guess karo")
            continue

        attempts = attempts + 1

        if guess == secret_number:
            print("you won !")
            print("total attempts:", attempts)
        elif guess < secret_number:
            print("too low")
        else:
            print("too high")
    play_again = input("Dobara khelna hai? (yes/no): ").strip().lower()
    while play_again not in ("yes", "no"):
         play_again = input("Invalid input. Please enter 'yes' or 'no': ").strip().lower()
    if play_again == "no":
        print("goodbye")   
        break

  
