import random

list1 = []

for i in range(0, 41):

    num = random.randint(0, 100)

    list1.append(num)

list1.sort()


def binarySearch(list1, target):
    length = len(list1)
    l = 0
    r = length - 1
    while (l <= r):
        middle = (l+r)//2
        if (list1[middle] == target):
            return middle
        elif (list1[middle] > target):
            r = middle - 1
        elif (list1[middle] < target):
            l = middle + 1
        else:
            return -1


target = 10
result = binarySearch(list1, target)

print(result)
