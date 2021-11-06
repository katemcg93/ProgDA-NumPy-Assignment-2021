import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()

#Chi square distribution

sns.kdeplot(random.chisquare(df = 1, size = 1000), ax = ax, color = '#DAB6C4', label = "1 Degree of Freedom")
ax2 = ax.twinx()
ax2.get_yaxis().set_ticks([])
sns.kdeplot(random.chisquare(df = 2, size = 1000), ax =ax2, color = '#7B886F', label = "2 Degrees of Freedom")
ax3 = ax.twinx()
ax3.get_yaxis().set_ticks([])
sns.kdeplot(random.chisquare(df = 3, size = 1000), ax = ax3, color = '#B4DC7F', label = "3 Degrees of Freedom" )
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc=0)
plt.savefig("chisquare.png")
plt.close()

#Uniform Distribution
#Generating multiple plots to show effect of sample size
#Expect that as sample size increases, plot will more closely resemble a normal distribution - 
#equal probability that any of the numbers between 1 and 10 will be chosen
uniformdist10 = np.random.uniform(size = 10, high = 1, low = 10)
uniformdist1000 = np.random.uniform(size = 1000, high = 1, low = 10)
uniformdist10000 = np.random.uniform(size = 10000, high = 1, low = 10)
uniformdist100000 = np.random.uniform(size = 100000 , high = 1, low = 10)

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

#Binomial Distribution
#Simulating one Coin Toss done 100000 times
#Changing Probability to see effect on distribution
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
cointest25 = np.random.binomial(n = 10, p = 0.25, size = 100000)
cointest50 = np.random.binomial(n = 10, p = 0.50, size = 100000)
cointest75 = np.random.binomial(n = 10, p = 0.75, size = 100000)
cointest100 = np.random.binomial(n = 10, p = 1, size = 100000)
sns.histplot(cointest25, ax = ax1)
sns.histplot(cointest50, ax = ax2)
sns.histplot(cointest75, ax = ax3)
sns.histplot(cointest100, ax = ax4)
plt.tight_layout()
plt.savefig("binomial distribution.png")
plt.close()