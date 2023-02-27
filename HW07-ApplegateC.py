# The Barking Lot cill calculator Christian Applegate
# declaring variables and ranges
litRange = 15
medRange = 30
heavyRange = 80
ultRange = 81
lightWeight = 55
medWeight = 75
heavyWeight = 105
ultraWeight = 125

# user input to calculate data
dogName = input("What is the dog's name? ")
ownerName= input("What is the owners's name? ")
breed = input("What type of breed is the dog? ")
age = input("How old is the dog? ")
dogWeight = int(input("How much does the dog weigh? "))

# calculating price for services
if dogWeight <= litRange:
    servCharge = lightWeight
else:
    if dogWeight <= medRange:
        servCharge = medWeight
    else:
        if dogWeight <= heavyRange:
            servCharge = heavyWeight
        else:
            if dogWeight >= ultRange:
                servCharge = ultraWeight

# display receipt
print("Owner Name: " + str(ownerName))
print("Dog Name: " + str(dogName))
print("Dog Breed: " + str(breed))
print("Dog Age: " + str(age))
print("Dog Weight: " + str(dogWeight))
print("Total: $" + str(servCharge))