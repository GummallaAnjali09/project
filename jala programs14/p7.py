try:
    file = open("example.txt", "r")
    print("File opened successfully.")
    result = 10 / 0
except FileNotFoundError:
    print("The file was not found.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This block will always be executed, whether an exception occurs or not.")
    try:
        file.close()
        print("File closed.")
    except NameError:
        print("File was not opened.")
