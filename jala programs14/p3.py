def dnumbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

class Main:
    def run(self):
        try:
            result = dnumbers(10, 0)
            print("Result:", result)
        except ZeroDivisionError as e:
            print("Error:", e)

main = Main()
main.run()
