# Function that greets user after inputting name
def welcome_message(name):
    return f"{name}, welcome to the Data Engineering course. The course will be a great learning experience!"

# Function that comments on color inputted by user
def favorite_color(color):
    return f"{color} is an amazing color!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(welcome_message(name))
    color = input("Enter your favorite color: ")
    print(favorite_color(color))

