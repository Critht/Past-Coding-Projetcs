# code for determining if pancakes can be made or a grocery store trip is needed, Christian Applegate, 4/1/2022

# declaring our variables and constants
import sys
MIN_FLOUR = 1.50 # cups
MIN_MILK = 1 # cups
MIN_EGG = 1
MIN_BUTTER = 3 # TBS
MIN_SALT = 0.50 # TSP
MIN_SUGAR = 1 # TBS
avFlour = 0
avMilk = 0
avEgg = 0
avButter = 0
avSalt = 0
avSugar = 0
# declaring list commands, files, and lists
listCounter = 0
groceryList = []
nextLine = None
file = open('Grocery List.txt', 'w')

print("Good morning! Ready to make some pancakes?", "\n")
print("Please check your kitchen for the following ingredients: ", "\n", "Flour", "\n", "Milk", "\n", "Eggs", "\n", "Butter", "\n", "Salt")

# user input to check fridge for ingredients
avFlour = input("For a simple serving, the recommended amount of Flour is 1.5 cups. Please, check your kitchen for flour and input the amount. ")
if avFlour >= str(MIN_FLOUR):
    print(str(avFlour), "cups should be enough. Let's move on")
else:
    listCounter +=1
    groceryList.insert(1, "Flour") # adding it to the list
    print(str(avFlour), "cup will not be enough. I will put it on your list. Let's see if we need anything else from the store.")

# Next ingredient
avMilk = input("For a simple serving, the recommended amount of Milk is 1 cup. Please, check your kitchen for Milk and input the amount. ")
if avMilk >= str(MIN_MILK):
    print(str(avMilk), "cups should be enough. Let's move on")
else:
    listCounter += 1
    groceryList.insert(2, "Milk") # adding it to the list
    print(str(avMilk), "cup will not be enough. I will put it on your list. Let's see if we need anything else from the store.")

# Next ingredient
avEgg = input("For a simple serving, the recommended amount is 1 egg. Please, check your kitchen for any eggs and input the amount. ")
if avEgg >= str(MIN_EGG):
    print(str(avEgg), "eggs should be enough. Let's move on")
else:
    listCounter += 1
    groceryList.insert(3, "Eggs") # adding it to the list
    print("No eggs? I will put it on your list. Let's see if we need anything else from the store.")

# next ingredient
avButter = input("For a simple serving, the recommended amount of butter is 3 Tbs. Please, check your kitchen for butter and input the amount. ")
if avButter >= str(MIN_BUTTER):
    print(str(avButter), "Tbs. should be enough. Let's move on")
else:
    listCounter += 1
    groceryList.insert(4, "Butter") # adding it to the list
    print("No butter? I will put it on your list. Let's see if we need anything else from the store.")

# next ingredient
avSalt = input("For a simple serving, the recommended amount of Salt is 1/2 Tsp. Please, check your kitchen for salt and input the amount. ")
if avSalt >= str(MIN_SALT):
    print(str(avSalt), "Tsp. should be enough. Let's move on.")
else:
    listCounter += 1
    groceryList.insert(5, "Salt") # adding it to the list
    print("No Salt? I will put it on your list. Now would be the best time to go to the store.")
    
    # next ingredient
avSugar = input("For a simple serving, the recommended amount of Sugar is 1 Tbs. Please, check your kitchen for sugar and input the amount. ")
if avSugar >= str(MIN_SUGAR):
    print(str(avSugar), "Tbs. should be enough.")
else:
    listCounter += 1
    groceryList.insert(6, "Sugar") # adding it to the list
    print("No Sugar? I will put it on your list. Now would be the best time to go to the store.")
    
# Now that all the info is gathered we will see if you can make pancakes.
if listCounter >= 1:
    print('\n', "Sorry, looks like you cannot make pancakes.", "\n", "Here is your grocery list:")
    for item in groceryList:
        file.write(item + '\n')
    file = open('Grocery List.txt', 'r')
    output = file.read()
    print(output)
    file.close()
    sys.exit
else: # Now the code will read the step by step instruction from a text file within the same location as this code
    print('\n', 'Looks like we are able to make pancakes!', '\n' "Please follow along:", '\n')
    try:
        file2 = open("Pancake.txt", 'r')
        while True:
            nextLine = file2.readline().strip()
            if (nextLine == ""):
                break
            print(nextLine, '\n')
            
    except IOError as e:
        print('\n' , 'CANNOT OPEN FILE. PLEASE CHECK IF FILE EXISTS AND IS IN THE SAME LOCATION AS THIS FILE', '\n')
