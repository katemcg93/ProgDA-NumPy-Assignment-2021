import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
poissondist1 = np.random.poisson(lam = 1, size = 10)
poissondist2 = np.random.poisson(lam = 5, size = 10)
poissondist3 = np.random.poisson(lam = 8, size = 10)

fig, ax = plt.subplots()
rng = np.random.default_rng(12345)

np.random.seed(100)

plt.suptitle("KDE Plot Poisson Distributions")
sns.kdeplot(poissondist1, ax = ax, color = '#FF7B9C', label = "Lam: 1")
ax2 = ax.twinx()
ax2.get_yaxis().set_ticks([])
sns.kdeplot(poissondist2, ax = ax2, color = '#607196', label = "Lam: 5")
ax3 = ax.twinx()
ax3.get_yaxis().set_ticks([])
sns.kdeplot(poissondist3, ax = ax3, color = '#FFC759', label = "Lam: 8")
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax2.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc=0)
plt.savefig("poisson.png")
plt.close()




