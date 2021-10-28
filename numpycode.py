import numpy as np

#First Section: for part 1 of assessment
#Code for creating and manipulating numpy arrays

#Arrays of different dimensions
oneDArray = np.array ([1,2,3])
print(oneDArray)

twoDArray = np.array ([(1,2), (3,4)])
print(twoDArray)

threeDArray = np.array ([(1,2), (3,4), (5,6)])

#Zeros/Ones function: Create arrays filled with ones and zeros
zerosArray = np.zeros((3,10))
print(zerosArray)

onesArray = np.ones((3,10))
print(onesArray)

#Creating an empy array
emptyArray = np.empty(2)
print(emptyArray)

#Passing type argument to array
floatTypeArray = np.array([1,2,3,4], dtype = 'f')
print(floatTypeArray.dtype)

#Changing type of existing array from float to string
stringTypeArray = floatTypeArray.astype('S')
print(stringTypeArray.dtype)


#Arange function: creates an array within specified value range
#Arange function takes three arguments - start, stop and step - count up in 2s,3s etc

twoStep = np.arange(1,10,2)
print(twoStep)

threeStep = np.arange(0,100,3)
print(threeStep)

#Linspace function - similar to arange but returns a specified amount of evenly spaced numbers
#Below example will provide 5 evenly spaced numbers between 20 and 40
evenSpace = np.linspace(20,40,5)
print(evenSpace)
