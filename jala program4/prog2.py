def avgarr(arr):
    total=sum(arr)
    avg=total/len(arr)
    return avg
n=int(input("enter  numbers in list"))
arr=[]
for i in range(1,n+1):
    num=int(input())
    arr.append(num)
print(avgarr(arr))
