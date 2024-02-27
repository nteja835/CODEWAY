import random

def generate_pass(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    pass1= ''.join(random.choice(characters) for i in range(length))
    return pass1
def pass_generator():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive length.")
            return
        else:
            pass1 = generate_pass(length)
            print("Generated Password:", pass1)

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

if __name__ == "__main__":
    pass_generator()
