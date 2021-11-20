#Code to show differences between shuffle, permute and permuted
import numpy as np
myarray = np.arange(1,10).reshape(3,3)
rng = np.random.default_rng()
print("Original Array : {} ".format(myarray))

#Along axis 0 - will change the order of the dimensions/groups but not individual elements
#Along axis 1 - will change the order of the elements but not the dimensions/groups
#Both methods will return new array
permute_ax0 = rng.permutation(myarray, axis = 0)
permute_ax1 = rng.permutation(myarray, axis = 1)
print("Permutation Axis 0: {}\n Permutation Axis 1: {}".format(permute_ax0,permute_ax1))

#Specified myarray as out array - means the numpy array order will be altered rather than returning a new array
#Axis 0 - will change the elements in the individual dimensions/groups of elements rather than just shuffling group order, and order of elements within group
#Axis 1 - will take the already shuffled myarray and shuffle the elements within the group
permuted_ax0 = rng.permuted(myarray, axis = 0, out = myarray)
print("Permuted Axis 0: {}".format(myarray))
permuted_ax0 = rng.permuted(myarray, axis = 1, out = myarray)
print("Permuted Axis 1 : {}".format(myarray))

#The shuffle method will alter the original array without specifying an out paramter
#Axis 0 - will shuffle the groups but not the element order within them
#Axis 1 - will shuffle the elements but not the group order

rng.shuffle(myarray, axis = 0)
print("Array shuffled along axis 0: {}".format(myarray))

rng.shuffle(myarray, axis = 1)
print("Array shuffled along axis 1: {}".format(myarray))
