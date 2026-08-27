def welcome_message(name):
    return f"{name}, welcome to the Data Engineering course. The course will be a great learning experience!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(welcome_message(name))
