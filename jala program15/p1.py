
fruits = {
    1: "Apple",
    2: "Banana",
    3: "Cherry",
    4: "Date",
    5: "Elderberry"
}
fruits[6] = "Fig"
fruits[7] = "Grapes"
print("After adding values:", fruits)
fruits[2] = "Blueberry"
print("After updating value:", fruits)
print("Accessing fruit with ID 3:", fruits[3])
nested_fruits = {
    "Citrus": {8: "Orange", 9: "Lemon"},
    "Berries": {10: "Strawberry", 11: "Raspberry"},
    "Tropical": {12: "Mango", 13: "Pineapple"}
}
print("Fruits in Citrus category:", nested_fruits["Citrus"])
print("Fruit with ID 8 in Citrus category:", nested_fruits["Citrus"][8])
print("Keys in fruits dictionary:", fruits.keys())
print("Keys in nested_fruits dictionary:", nested_fruits.keys())
del fruits[5]
print("After deleting fruit with ID 5:", fruits)
