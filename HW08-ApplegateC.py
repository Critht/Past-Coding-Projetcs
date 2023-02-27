# Code for calcluating tuition in a span of 10 years, 3/14/2022, HW08
# Declaring constants and variables

head1 = "Your tuition for the year: " # displays our output. Will include year and cost
TUITION = 10000
yearRate = 0.03
yearRateInc = 0
tuitionOverTime = 0
tuitionTotal = 0
tuitionCounter = 1
YEAR = 2022
yearCounter = 0
MAX_LOOP = 10

# loop statement
while yearCounter <= MAX_LOOP:
    print(head1 + str(YEAR))
    tuitionOverTime = TUITION * tuitionCounter
    yearRate = yearRate + yearRateInc
    tuitionTotal = tuitionOverTime + (TUITION * yearRate)
    print("$" + str(tuitionTotal))
    yearRateInc = yearRate
    YEAR = YEAR + 1
    tuitionCounter += 1
    yearCounter += 1