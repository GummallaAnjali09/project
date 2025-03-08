def containval(arr, val):
    return val in arr
n=int(input("enter  numbers in list"))
arr=[]
for i in range(1,n+1):
    num=int(input())
    arr.append(num)
ele=int(input("enter a element"))
print(containval(arr,ele))


