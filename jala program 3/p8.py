n=int(input())
s=0
t=n
r=0
while n>0:
    r=n%10
    s+=r*r*r
    n=n//10
if t==s:
    print(t,"is an Armstrong number")
else:
    print(t,"is not an Armstrong number")
    
