import re
s= "Hello, World!"
patt="Hello"  
match = re.match(patt,s)

if match:
    print("Match found")
