def findex(arr, element):
    if element in arr:
        return arr.index(element)
    return -1  
n=int(input("enter  numbers in list"))
arr=[]
for i in range(1,n+1):
    num=int(input())
    arr.append(num)
ele=int(input("enter a element"))
print(findex(arr,ele))
