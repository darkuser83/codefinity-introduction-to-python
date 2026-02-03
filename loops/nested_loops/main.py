produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries = [["Tomatoes", "Lettuce"],["Milk", "Cheese"]]
print(groceries)
for section in groceries:
    for item in section:
        print(f"Item Name : {item}")
    