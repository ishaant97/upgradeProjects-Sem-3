# function to calculate BMI
def calculateBmi(height, weight):
    bmi = weight / (height ** 2) * 703  # Calculated BMI using the formula
    return bmi

# function to determine the child's nutritional status based on BMI


def isChildUnderNourished(bmi):
    if bmi <= 16:
        return "Severely Underweight"
    elif 16 < bmi <= 18.5:
        return "Underweight"
    elif 18.5 < bmi <= 25:
        return "Healthy"
    elif 25 < bmi <= 30:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
    else:
        pass


print("Welcome To Child Based Nutrients Calculator")

name = input("Enter your child's name : ")

# Get and validate the child's age
while True:
    age = int(input("Enter your child's age : "))
    if 0 < age <= 8:
        break
    else:
        print("Please Enter the age between 1 to 8.")
        continue

gender = input("Enter gender of your child(male/female) : ")
weight = float(input("Enter your child's weight in pounds : "))
height = float(input("Enter your child's height in inches : "))

# Calculated BMI and determine the child's status based on BMI
BMI = round(calculateBmi(height, weight), 1)
childStatus = isChildUnderNourished(BMI)
