def minmaxfun(arr):
    if not arr:
        return None 
    
    small = min(arr)
    large = max(arr)
    
    return small,large


arr=list(map(int,input().split()))
small, large=minmaxfun(arr)
print("Minimum value is:", small)
print("Maximum value is:", large)
