# code that reads contents of separate text files and calculates an average, Christian Applegate, 3-26-2022
# input file
item = open("ABC_Inventory.txt", "r")
itemData = None
descData = None
# while loop
while True:
    itemData = item.readline().strip()
    descData = item.readline().strip()
    priceData = item.readline().strip()
    if (itemData == ""):
        break
# Print Item name
    print("Item number: " + "\n" + itemData + "\n")
# Print Description name
    print("Item description: " + "\n" + descData + "\n")
# Print Price listing
    print("Item price: " + "\n" + priceData + "\n")

