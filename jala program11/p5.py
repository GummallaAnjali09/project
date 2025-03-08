fname = "Fileop.txt"

with open(fname, "r") as file:
    index = int(input("Enter the index to jump to: "))  
    file.seek(index)  
    content = file.read(10)
    print(f"Reading from index {index}:")
print(content)
