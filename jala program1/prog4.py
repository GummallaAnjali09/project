x=10
def print_var():
    x=20
    print("Local variable x:",x)
    print("Global variable x:",globals()['x'])
print_var()
print("Global variable x:",x)
