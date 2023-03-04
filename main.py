import random

def password_generator(length):
    """Generate a random password of specified length."""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print("Your new password is:", password_generator(length))
