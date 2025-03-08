def sumarr(arr):
    return sum(arr)
n=int(input("enter  numbers in list"))
arr=[]
for i in range(1,n+1):
    num=int(input())
    arr.append(num)
print(sumarr(arr))
