def copyarr(arr):
    return arr.copy()
n=int(input("enter  numbers in list"))
arr=[]
s=[]
for i in range(1,n+1):
    num=int(input())
    s.append(num)
print(copyarr(s))

