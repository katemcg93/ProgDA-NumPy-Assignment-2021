#This programme is to illustrate the difference in speed between NumPy and Python lists
#Will be creating 2 lists and arrays of equal size, iterating through elements and multiplying them by each other
#And printing time taken to complete each operation for both
#Source: GeeksforGeeks (full reference in Jupyter Notebook)

import numpy as np
import time
from sys import getsizeof

size = 1000000

list1 = range(size)
list2 = range(size)

#Need to get current time to second to subtract from time taken to complete operation
startTime = time.time()
print(startTime)

newlist = []

#This code is zipping list 1 and 2 together - mapping each list1 value to its corresponding list2 value and multiplying them
#Then adding them to new list
for a,b in zip(list1,list2):
    newlist.append(a*b)

TimeNow = time.time()
TimeTaken = TimeNow - startTime
print("Time taken to complete in seconds: {}".format(TimeTaken))

#Declaring Arrays
array1 = np.arange(size)  
array2 = np.arange(size)

startTimeNumpy = time.time()

NewArray = array1* array2

TimeNowNumpy = time.time()
TimeTakenNumpy = TimeNowNumpy - startTimeNumpy
print("Time taken to complete in seconds: {}".format(TimeTakenNumpy))
print("Time difference in seconds: {}".format(TimeTaken - TimeTakenNumpy))


#Checking difference in memory consumption between numpy array and python list
totalMemoryList = getsizeof(newlist)
totalMemoryNumpy = getsizeof(NewArray)

print("Total memory consumed by Python List: {} bytes".format(totalMemoryList))
print("Total memory consumed by Numpy Array: {} bytes".format(totalMemoryNumpy))
print("Memory difference in bytes: {}".format(totalMemoryList - totalMemoryNumpy))

