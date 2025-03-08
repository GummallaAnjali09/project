fname = "Fileop.txt"  

with open(fname, "r") as file:  
    content = file.read()  

print("File content:\n",content)
