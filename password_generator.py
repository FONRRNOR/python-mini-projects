import random
import string

def get_user_preferences():
    print("PASSWORD GENERATOR")
    
    while True:
        try:
            length = int(input("Enter password length (minimum 4 characters): "))
            if length < 4:
                print("Password should be at least 4 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    if not any([include_upper, include_lower, include_digits, include_symbols]):
        print("You must select at least one character type.")
        return get_user_preferences()
    
    return length, include_upper, include_lower, include_digits, include_symbols

def build_character_pool(upper, lower, digits, symbols):
    pool = ""
    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digits:
        pool += string.digits
    if symbols:
        pool += string.punctuation
    return pool

def generate_password(length, pool):
    password = ''.join(random.choice(pool) for _ in range(length))
    return password

def main():
    length, upper, lower, digits, symbols = get_user_preferences()
    pool = build_character_pool(upper, lower, digits, symbols)
    
    while True:
        try:
            amount = int(input("How many passwords would you like to generate? "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    print("\nGenerated Passwords:")
    for i in range(amount):
        pwd = generate_password(length, pool)
        print(f"{i+1}. {pwd}")

if __name__ == "__main__":
    main()