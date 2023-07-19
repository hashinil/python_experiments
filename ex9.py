user_input = input("What is your name: ")
if 'h' in user_input:
    print("hello, you have H in your name")

user_input = input("What is your name: ")
if 's' in user_input or 'a' in user_input:
    print("hello, you have S or A in your name")

user_input = input("What is your name: ")
if 'k' in user_input and 'a' in user_input:
    print("hello, you have K and A in your name")

user_input = input("What is your name: ")
if 'i' not in user_input:
    print("hello, you have no I in your name")