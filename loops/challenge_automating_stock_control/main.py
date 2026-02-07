# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}
discount_threshold = 100
print("Processing Started")
for item in inventory:
    stocks = inventory.get(item)
    print(f"Processing {item}")
    current = stocks[0] 
    #print(current)
    minimum = stocks[1]
    #print(minimum)
    restock = stocks[2] 
    #print(restock)
    sale = stocks[3]
    #print(sale)
    while minimum > current:
        current = current + restock
        #print(current)
        inventory[item]=[current, minimum, restock, sale]
        if (current > discount_threshold):
            sale = True
            inventory[item]=[current, minimum, restock, sale]
            #print(sale)
print("Processing Completed")