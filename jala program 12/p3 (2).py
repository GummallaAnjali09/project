class Ex:
    def __init__(self, a):
        print("Public Constructor Called")
        self.public_var = a
    def _protected_init(self, b):
        print("Protected Constructor Called")
        self._protected_var=b
    def __private_init(self, c):
        print("Private Constructor Called")
        self.__private_var=c
    def display(self):
        print(f"Public Var:",self.public_var)
        print(f"Protected Var:",getattr(self, '_protected_var', 'Not Accessible'))
        print(f"Private Var:",getattr(self, '_Example__private_var', 'Not Accessible'))
obj = Ex("Public Value")
obj._protected_init("Protected Value")
obj._Ex__private_init("Private Value")
obj.display()
