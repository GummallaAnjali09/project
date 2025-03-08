try:
    file = open("file.txt", "r")
    print(file.read())
except IOError:
    print("Error raised while trying to read the file")
finally:
    print("End of the program.")
