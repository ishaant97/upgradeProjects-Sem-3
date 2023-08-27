import random

# Create an empty list to store random numbers
list1 = []

# Generate 41 random numbers between 0 and 100 (inclusive) and store them in list1
for i in range(0, 41):
    num = random.randint(0, 100)
    list1.append(num)

# Sort the list in ascending order
list1.sort()

# Define a function for binary search


def binarySearch(list1, target):
    length = len(list1)
    l = 0
    r = length - 1
    while (l <= r):
        middle = (l+r)//2
        if (list1[middle] == target):
            return middle  # Target found at index 'middle'
        elif (list1[middle] > target):
            r = middle - 1  # Adjust the right boundary
        else:
            l = middle + 1  # Adjust the left boundary

    return -1  # Target not found


# Define the target value to search for
target = 10

# Call the binarySearch function to find the target in the sorted list
result = binarySearch(list1, target)

# Print the result of the search
print(result)
