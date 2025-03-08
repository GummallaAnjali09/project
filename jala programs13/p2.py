class OverloadDemo:
    def display(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            print(f"Single integer argument: {args[0]}")
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], float):
            print(f"String and float arguments: {args[0]}, {args[1]}")
        else:
            print("Invalid arguments")
demo = OverloadDemo()
choice = int(input("Enter 1 to pass an integer, 2 to pass a string and a float: "))

if choice == 1:
    num = int(input("Enter an integer: "))
    demo.display(num)
elif choice == 2:
    text = input("Enter a string: ")
    decimal = float(input("Enter a float number: "))
    demo.display(text, decimal)
else:
    print("Invalid choice")      
