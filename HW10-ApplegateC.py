# code for counting attendants in certain classes, Christian Applegate, 3/20/2022

# declare arrays
classes = ["Yoga 1", "Yoga 2", "Children's Yoga", "Prenatal Yoga", "Senior Yoga"]

# declaring variables
head1 = ("Please enter class number for ")
head2 = ("How many plan on attending class ")

class1 = input(str(head1) + "Yoga 1. ")
class2 = input(str(head1) + "Yoga 2. ")
class3 = input(str(head1) + "Children's Yoga. ")
class4 = input(str(head1) + "Prenatal Yoga. ")
class5 = input(str(head1) + "Senior Yoga. ")
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
# counting requests for classes
count1 = input(str(head2) + str(class1) + "? ")
count2 = input(str(head2) + str(class2) + "? ")
count3 = input(str(head2) + str(class3) + "? ")
count4 = input(str(head2) + str(class4) + "? ")
count5 = input(str(head2) + str(class5) + "? ")
# output the class number, number of attendants, and name of class
print("Class number: " + str(class1) + " for Yoga 1 has " + str(count1) + " in attendance.")
print("Class number: " + str(class2) + " Yoga 2 has " + str(count2) + " in attendance.")
print("Class number: " + str(class3) + " Children's Yoga has " + str(count3) + " in attendance.")
print("Class number: " + str(class4) + " Prenatal Yoga has " + str(count4) + " in attendance.")
print("Class number: " + str(class5) + " Senior Yoga has " + str(count5) + " in attendance.")