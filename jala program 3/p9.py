n = int(input())
count=0
if n< 2:  
    print(n, "is not a prime number")  
else:  
    for i in range(1,n+1):  
        if n%i == 0:
            count+=1
    if count==2:
        print(n,"is prime number")
    else:
        print(n,"is not prime number")

        
    
