def insertele(arr, ind, val):
    arr.insert(ind, val)
    return arr
n=int(input("enter  numbers in list"))
arr=[]
for i in range(1,n+1):
    num=int(input())
    arr.append(num)
val=int(input("enter a value"))
ind=int(input("enter an index"))
print(insertele(arr,ind,val))
