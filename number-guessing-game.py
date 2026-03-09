import random

def choose_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy (1-50, 10 guesses)")
    print("2. Medium (1-100, 7 guesses)")
    print("3. Hard (1-500, 5 guesses)")
    
    while True:
        choice = input("Enter choice (1-3): ")
        if choice == '1':
            return 50, 10
        elif choice == '2':
            return 100, 7
        elif choice == '3':
            return 500, 5
        else:
            print("Invalid choice. Try again.")

def give_hint(secret, guess):
    diff = abs(secret - guess)
    
    if diff == 0:
        return "correct"
    elif diff <= 3:
        return "Very close!"
    elif diff <= 10:
        return "Close!"
    else:
        return "Far!"

def calculate_score(max_attempts, attempts_used):
    return (max_attempts - attempts_used + 1) * 10

def play_game():
    max_number, max_attempts = choose_difficulty()
    secret_number = random.randint(1, max_number)
    attempts = 0
    
    print(f"\nI have selected a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts to guess it!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts+1}: Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > max_number:
                print("Out of range!")
                continue
            
            hint = give_hint(secret_number, guess)
            
            if hint == "correct":
                score = calculate_score(max_attempts, attempts)
                print(f"Correct! You guessed the number in {attempts} tries.")
                print(f"Your score: {score}")
                break
            else:
                if guess > secret_number:
                    print("Too high!", hint)
                else:
                    print("Too low!", hint)
                
                print(f"Remaining attempts: {max_attempts - attempts}")
        
        except ValueError:
            print("Please enter a valid number.")
    
    else:
        print(f"\nGame Over! The correct number was {secret_number}")

def main():
    print("Welcome to the Advanced Number Guessing Game!")
    
    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()