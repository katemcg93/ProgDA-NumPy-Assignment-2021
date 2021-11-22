import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
random_numbers = np.random.randint(1, 100, size = 5)
print(random_numbers)

sns.histplot(random_numbers)
plt.show()
