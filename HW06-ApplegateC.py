# Rental car calculator Christian Applegate HW06
# declaring variables
BASECHARGE = 65
COMPACT = 0
STANDARD = 10
SUV = 15
VAN = 25
MAXRENTDAYS = 7
RENTDISCOUNT = 20
# inputs asking for customer info and vehicle choice
custName = (input("What is the customer name? "))
vehicleChoice = int(input("What kind of car are you looking for: compact(1), standard(2), suv(3), van(4)? "))
# calculate charges
if (vehicleChoice == 1):
    vehiclePrice = COMPACT + BASECHARGE
elif(vehicleChoice == 2):
    vehiclePrice = STANDARD + BASECHARGE
elif(vehicleChoice == 3):
    vehiclePrice = SUV + BASECHARGE
elif(vehicleChoice == 4):
    vehiclePrice = VAN + BASECHARGE

# discount calculation and final price
rentDays = int(input("How long will you be renting with us? "))
if (rentDays > MAXRENTDAYS):
    discountPrice = vehiclePrice - (vehiclePrice * RENTDISCOUNT / 100)
    print(str(custName) + " your total is $" + str(discountPrice))
elif (rentDays <= MAXRENTDAYS):
    print(str(custName) + " your total is $" + str(vehiclePrice))