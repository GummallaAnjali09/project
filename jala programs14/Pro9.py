try:
    file = open("file.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File Not Found")
finally:
    print("End of the program.")
