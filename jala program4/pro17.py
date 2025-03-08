class ArrayCon:
    def cele(self, ar):
        if 12 in ar and 23 in ar:
            return True
        else:
            return False


a= ArrayCon()
print("Enter list elements:")
l=list(map(int,input().split()))

if a.cele(l):
    print("Given elements found")
else:
    print("Given elements not found")
