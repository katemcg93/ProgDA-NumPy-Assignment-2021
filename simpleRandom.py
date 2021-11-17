import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

#Setting up generator to use default bit generator - PCG64
rng = np.random.default_rng(12345)
randomints = rng.integers(low = 1, high = 10,size = 100000, endpoint = True)
print(randomints)
#Uniform Distribution
#Generating multiple plots to show effect of sample size
#Expect that as sample size increases, plot will more closely resemble a normal distribution - 
#equal probability that any of the numbers between 1 and 10 will be chosen
uniformdist10 = rng.integers(size = 10, low = 1, high =5)
uniformdist1000 = rng.integers(size = 1000, low = 1, high =5)
uniformdist10000 = rng.integers(size = 10000, low = 1, high = 5)
uniformdist100000 = rng.integers(size = 100000 , low = 1, high = 5) 

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.suptitle("Effect of Sample Size on Uniform Distribution")
ax1.hist(uniformdist10, color = '#7A82AB')
ax1.set_title("10 Samples")
ax2.hist(uniformdist1000, color = '#307473')
ax2.set_title("1000 Samples")
ax3.hist(uniformdist10000, color = '#12664F')
ax3.set_title("10000 Samples")
ax4.hist(uniformdist100000, color = '#C6D4FF')
ax4.set_title("100000 Samples")
plt.tight_layout()
plt.savefig("uniform distribution.png")
plt.close()

ct_uniform10 = 5 * rng.random (10) + 0
ct_uniform1000 = 5 * rng.random (1000) + 0
ct_uniform10000 = 5 * rng.random (10000) + 0
ct_uniform100000 = 5 * rng.random (100000) + 0

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.suptitle("Effect of Sample Size on Uniform Distribution")
ax1.hist(ct_uniform10, color = '#7A82AB')
ax1.set_title("10 Samples")
ax2.hist(ct_uniform1000, color = '#307473')
ax2.set_title("1000 Samples")
ax3.hist(ct_uniform10000, color = '#12664F')
ax3.set_title("10000 Samples")
ax4.hist(ct_uniform100000, color = '#C6D4FF')
ax4.set_title("100000 Samples")
plt.tight_layout()
plt.savefig("ct_uniform distribution.png")
plt.close()

selected_probability = rng.choice(5, 1000, p = [0.0, 0.0,0.2,0.0, 0.8])
standard_probability = rng.choice(5, 1000)

fig, ((ax1), (ax2)) = plt.subplots(1, 2)
ax1.hist(standard_probability, color = '#7A82AB')
ax1.set_title("Uniform Probability")
ax2.hist(selected_probability, color = '#307473')
ax2.set_title("Non Uniform Probability")
plt.savefig("prob_choice.png")

random_byte_array  = np.random.default_rng().bytes(30)
print(type(random_byte_array))
print(random_byte_array)
print(random_byte_array.decode('ISO-8859-1'))

permute_array = np.arange(10)
print(permute_array)

print(rng.permutation(permute_array))