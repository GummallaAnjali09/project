fname = "Fileop.txt"  
txt = input("Enter text to write to the file: ")  

with open(fname, "w") as file:  
    file.write(txt)  

print("Text written to", fname, "successfully.")
