fname = "Fileop.txt"

with open(fname, "r") as file:
    print("Reading first 10 characters:")
    print(file.read(10))
    print("\nCurrent position in file:", file.tell())  
    print("\nMoving back to the 5th character...")
    file.seek(5)
    print("\nReading 10 characters from position 5:")
    print(file.read(10)) 
