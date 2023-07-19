try:
    width = float(input("Enter width: "))
    length = float(input("Enter length: "))

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number: ")
