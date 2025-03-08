class OverloadExample:
    def add(self, a, b):
        if isinstance(a, str) and isinstance(b, str):
            return a + " " + b  # Concatenation if both are strings
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b  # Addition if both are numbers
        else:
            return "Invalid input types!"
obj = OverloadExample()
val1 = input("Enter first value: ")
val2 = input("Enter second value: ")
try:
    val1 = float(val1) if '.' in val1 else int(val1)
    val2 = float(val2) if '.' in val2 else int(val2)
except ValueError:
  pass
result = obj.add(val1, val2)
print("Result:", result)      
