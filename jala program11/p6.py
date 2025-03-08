fname = "Fileop.txt"  
file = open(fname, "r")  
print(f"{fname} has read access.")  
file.close()  
file = open(fname, "a")  
print(f"{fname} has write access.")
file.close()
