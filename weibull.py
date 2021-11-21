import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


weibull01 = np.random.weibull(a = 0.1, size = 10000)
weibull1 = np.random.weibull(a = 1.0, size = 10000)
weibull2 = np.random.weibull(a = 2.0, size = 10000)
weibull3 = np.random.weibull(a = 3.0, size = 10000)


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
sns.despine()
plt.suptitle("Weibull Distribution - Effect of Increasing Scale")
ax1.set_title("Scale = 0.1", fontsize = 12)
ax2.set_title("Scale = 1.0", fontsize = 12)
ax3.set_title("Scale = 2.0", fontsize = 12)
ax4.set_title("Scale = 3.0", fontsize = 12)
sns.kdeplot(weibull01, ax = ax1, color = '#F86624', fill = True)
sns.kdeplot(weibull1, ax = ax2, color = '#EA3546', fill = True)
sns.kdeplot(weibull2, ax = ax3, color = '#662E9B', fill = True)
sns.kdeplot(weibull3, ax = ax4, color = '#43BCCD', fill = True)
plt.tight_layout()
plt.savefig("weibull distribution.png")
plt.show()
plt.close()

