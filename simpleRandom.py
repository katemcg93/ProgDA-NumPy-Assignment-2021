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
