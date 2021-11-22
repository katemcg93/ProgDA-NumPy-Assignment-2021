import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
random_numbers = np.random.randint(1, 100, size = 5)
print(random_numbers)

sns.histplot(random_numbers)
plt.show()

rng1 = np.random.default_rng(100)
rng2 = np.random.default_rng(45)

def random_array (x):
    random_numbers = x.integers(1,100,size = 5)
    return random_numbers

random_numbers1 = random_array(x = rng1)
random_number2 = random_array(x = rng2)
print(random_numbers1, "\n", random_number2)