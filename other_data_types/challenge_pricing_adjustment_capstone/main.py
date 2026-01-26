# Accessing nested data
# print(employee['skills'][1])  # Output: Machine Learning
# print(employee['address']['city'])  # Output: San Francisco


grocery_inventory = {
        "Milk": ("Dairy", 3.50, 8),
        "Eggs": ("Dairy", 5.50, 30),
        "Bread": ("Bakery", 2.99, 15),
        "Apples": ("Produce", 1.50, 50)    
}

egg_price = grocery_inventory.get("Eggs")

if egg_price[1] > 5:
    print("eggs are too expensive, reducing the price by $1.")
    #grocery_inventory["eggs"] = ("Dairy", 4.50, 30)
    grocery_inventory.update({
        "Eggs": 
        ("Diary", 
         4.50, 
         30)
        })
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({
    "Tomatoes": 
    ("Produce", 
     1.20, 
     30)
    })

print(f"inventory after adding tomatoes:{grocery_inventory}")

milk_stock = grocery_inventory.get("Milk")

if milk_stock[2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory.update({
        "Milk": 
        ("Produce", 
         3.50, 
         28)
        })
else:
    print("Milk has sufficient stock.")

apples_price = grocery_inventory.get("Apples")

if apples_price[1] > 2:
    print("Apples removed from inventory due to high price.")
    grocery_inventory.pop("Milk") 

print(f"Updated inventory:{grocery_inventory}")