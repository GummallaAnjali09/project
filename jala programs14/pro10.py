try:
    from module import NonExistentClass
except ImportError:
    print("Oops! The class or module is not exsted")
finally:
    print("End of the program.")
