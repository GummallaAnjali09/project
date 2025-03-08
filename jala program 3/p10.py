n=int(input())  
temp=n
r=0  

while temp>0:
    d=temp%10  
    r =(r*10)+d  
    temp//= 10  

if n==r:
    print("Palindrome")
else:
    print("Not a palindrome")
    

