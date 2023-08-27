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
# function to calculate calorie intake based on food quantities


def calEaten(foodDict):
    # Define calorie values for different food items
    milk = 1
    egg = 1.55
    rice = 1.3
    lentils = 1.13
    vegetable = 0.85
    meat = 1.43

    foodNames = list(foodDict.keys())  # Get a list of food items
    foodLength = len(foodNames)  # Calculate the number of food items

    totalCalEaten = 0

    # Iterate through each food item and calculate total calories eaten
    for i in range(0, foodLength):
        if foodNames[i] == "Milk":
            tempCal = foodDict.get("Milk")
            totalCalEaten = totalCalEaten + (tempCal * milk)
        elif foodNames[i] == "Egg":
            tempCal = foodDict.get("Egg")
            totalCalEaten = totalCalEaten + (tempCal * egg)
        elif foodNames[i] == "Rice":
            tempCal = foodDict.get("Rice")
            totalCalEaten = totalCalEaten + (tempCal * rice)
        elif foodNames[i] == "Lentils":
            tempCal = foodDict.get("Lentils")
            totalCalEaten = totalCalEaten + (tempCal * lentils)
        elif foodNames[i] == "Vegetable":
            tempCal = foodDict.get("Vegetable")
            totalCalEaten = totalCalEaten + (tempCal * vegetable)
        elif foodNames[i] == "Meat":
            tempCal = foodDict.get("Meat")
            totalCalEaten = totalCalEaten + (tempCal * meat)
        else:
            pass

    return totalCalEaten  # Return the total calorie intake

# function to determine the child's nutritional status based on calorie intake and age


def childStatusOnTheBasisOfCalIntake(calEatenByTheChild, age):
    if 0 < age <= 2:
        if calEatenByTheChild < 800:
            return "Under Nourished"
        else:
            return "Nourished"
    elif 2 < age <= 4:
        if calEatenByTheChild < 1400:
            return "Under Nourished"
        else:
            return "Nourished"
    elif 4 < age <= 8:
        if calEatenByTheChild < 1800:
            return "Under Nourished"
        else:
            return "Nourished"


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

# Display BMI and current nutritional status
print("BMI of your child is ", BMI)
print("Current status of your child is", childStatus)

# Get the number of times the child has eaten and input food details
timesEaten = int(input("Enter how many times your child has eaten : "))

foodEaten = {}  # Initialize a dictionary to store food and quantity

# Loop through each meal and input food and quantity
for i in range(0, timesEaten):
    food = input("Enter what your child has eaten : ").capitalize()
    quantity = float(input("Enter the quantity of the food (in grams) : "))
    # Store the food and its quantity in the dictionary
    foodEaten[food] = quantity

# Calculate total calories eaten by the child
calEatenByTheChild = calEaten(foodEaten)

# Determine if the child is nourished or undernourished based on calorie intake and age
nourishedOrUndernourished = childStatusOnTheBasisOfCalIntake(
    calEatenByTheChild, age)

# Display calorie intake and nutritional status
print("Calories eaten by your child is", calEatenByTheChild,
      "and he/she is", nourishedOrUndernourished)
