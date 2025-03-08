def duplicate(arr):
    dup = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in dup:
                dup.append(arr[i])
    return dup
arr=list(map(int,input().split()))
dup=duplicate(arr)
print("Duplicate values:", dup)
