def removeele(arr, value):
    if value in arr:
        arr.remove(value)
    return arr
n=int(input("enter  numbers in list"))
arr=[]
for i in range(1,n+1):
    num=int(input())
    arr.append(num)
ele=int(input("enter a element"))
print(removeele(arr,ele))
