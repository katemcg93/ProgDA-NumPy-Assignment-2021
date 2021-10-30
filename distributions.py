import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.chisquare(df = 1, size = 1000), kind = "kde")
sns.displot(random.chisquare(df = 2, size = 1000), kind = "kde")
sns.displot(random.chisquare(df = 3, size = 1000), kind = "kde")
plt.show()
