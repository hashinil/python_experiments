# No return
def greeting():
    message = "world"
    print("hello")
    new_message = message.capitalize()


greet = greeting()
print(greet)


# with return
def greeting_():
    message = "world"
    print("hello")
    new_message = message.capitalize()
    return new_message


greet = greeting_()
print(greet)
