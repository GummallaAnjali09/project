class Par:
    def __init__(self):
        self._pfield = "Protected Field in Parent" 
    def _pmethod(self):  
        print("Protected Method in Parent")

class SPClass:
    def aprotected(self):
        obj = Par()
        print("SamePackageClass:", obj._pfield) 
        obj._pmethod()

class Chi(Par):
    def aprotected(self):
        print("Child Class:", self._pfield)  
        self._pmethod()  

class NSubclass:
    def aprotected(self):
        obj = Par()
        print("NonSubclass:", obj._pfield)  
        obj._pmethod()

if __name__ == "__main__":
    print("Accessing from SamePackageClass:")
    spc = SPClass()
    spc.aprotected()

    print("\nAccessing from Child (Subclass in different 'package'):")
    child = Chi()
    child.aprotected()

    print("\nAccessing from NonSubclass (Different 'package'):")
    ns = NSubclass()
    ns.aprotected()
