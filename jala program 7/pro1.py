class A:
    def __init__(self):
        self.value = "Class A Variable"
    def method1(self):
        print("Method 1 from A")
    def method2(self):
        print("Method 2 from A")
    def show(self):
        print("Show from A")

class B(A):
    def __init__(self):
        super().__init__()
        self.value = "Class B Variable"
    def method3(self):
        print("Method 3 from B")
    def method4(self):
        print("Method 4 from B")
    def show(self):
        print("Show from B")

class C(B):
    def __init__(self):
        super().__init__()
        self.value = "Class C Variable"
    def method5(self):
        print("Method 5 from C")
    def method6(self):
        print("Method 6 from C")
    def show(self):
        print("Show from C")

class Main:
    def main():
        objA = A()
        objB = B()
        objC = C()
        objA.method1()
        objA.method2()
        objA.show()
        print(objA.value)
        objB.method1()
        objB.method3()
        objB.method4()
        objB.show()
        print(objB.value)
        objC.method1()
        objC.method3()
        objC.method5()
        objC.method6()
        objC.show()
        print(objC.value)
        ref = objB
        ref.show()
        print(ref.value)
        ref = objC
        ref.show()
        print(ref.value)

if __name__ == "__main__":
    Main.main()
