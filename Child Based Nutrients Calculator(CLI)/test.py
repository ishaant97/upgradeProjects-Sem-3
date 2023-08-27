# def calEaten(foodDict):
#     milk = 1
#     egg = 1.55
#     rice = 1.3
#     lentils = 1.13
#     vegetable = 0.85
#     meat = 1.43

#     foodNames = foodDict.keys()

#     print(foodNames)


# timesEaten = int(input("Enter how many times your child has eaten : "))

# foodEaten = {}
# for i in range(0, timesEaten):
#     food = input("Enter what you child has eaten : ")
#     quantity = float(input("Enter the quantity of the food(in grams) : "))
#     foodEaten[food] = quantity

# calEaten(foodEaten)


# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# list1 = list(thisdict.keys())

# print(thisdict.get("Brand"))


timesEaten = int(input("Enter the no. how many times your child has eaten : "))

foodEaten = {}  # Initialize a dictionary to store food and quantity

# Loop through each meal and input food and quantity
for i in range(0, timesEaten):
    food = input("Enter what your child has eaten : ").capitalize()
    print(food)
    quantity = float(input("Enter the quantity of the food (in grams) : "))
    # Store the food and its quantity in the dictionary
    foodEaten[food] = quantity
