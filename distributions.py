import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

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

fig, ax = plt.subplots()

plt.suptitle("Chi Square Probability Distribution - Effect of Degrees of Freedom")
#Generating three numpy arrays from Chi Square Distribution and plotting KDEs to see effect of df
sns.kdeplot(random.chisquare(df = 1, size = 1000), ax = ax, color = '#DAB6C4', label = "1 Degree of Freedom")
ax2 = ax.twinx()
ax2.get_yaxis().set_ticks([])
sns.kdeplot(random.chisquare(df = 10, size = 1000), ax =ax2, color = '#7B886F', label = "10 Degrees of Freedom")
ax3 = ax.twinx()
ax3.get_yaxis().set_ticks([])
sns.kdeplot(random.chisquare(df = 20, size = 1000), ax = ax3, color = '#B4DC7F', label = "20 Degrees of Freedom" )

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc=0)

plt.savefig("chisquare.png")
plt.close()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
#Removing top and right spines from plot
sns.despine()
plt.suptitle("Chi Square Distribution - Histogram with PDF")
#Plotting histograms for each distribution with KDE

sns.histplot(random.chisquare(df = 1, size = 100), ax = ax1, color = '#4B3F72', kde = True, edgecolor='#4B3F72', label = "1 Degree of Freedom")
ax1.set_title("1 Degree of Freedom", fontsize = 8)
sns.histplot(random.chisquare(df = 10, size = 100), ax = ax2, color = '#FFC857', kde = True, edgecolor = '#FFC857',  label = "10 Degrees of Freedom")
ax2.set_title("10 Degrees of Freedom", fontsize = 8)
sns.histplot(random.chisquare(df = 20, size = 100), ax = ax3, color = '#119DA4', kde = True, edgecolor = '#119DA4', label = "20 Degrees of Freedom")
ax3.set_title("20 Degrees of Freedom", fontsize = 8)

plt.tight_layout()
plt.savefig("chisquarehist.png")
plt.close()

#Binomial Distribution
#Changing Probability to see effect on distribution
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
sns.despine()
plt.suptitle("Binomial Distribution - Effect of Increasing P-value")
prob20 = np.random.binomial(n = 10, p = 0.20, size = 100000)
ax1.set_title("P = 0.2", fontsize = 8)
prob40 = np.random.binomial(n = 10, p = 0.40, size = 100000)
ax2.set_title("P = 0.4", fontsize = 8)
prob60 = np.random.binomial(n = 10, p = 0.60, size = 100000)
ax3.set_title("P = 0.6", fontsize = 8)
prob80 = np.random.binomial(n = 10, p = 0.80, size = 100000)
ax4.set_title("P = 0.8", fontsize = 8)
sns.histplot(prob20, ax = ax1, color = '#5BC0EB', kde = True)
sns.histplot(prob40, ax = ax2, color = '#FDE74C', kde = True)
sns.histplot(prob60, ax = ax3, color = '#9BC53D', kde = True)
sns.histplot(prob80, ax = ax4, color = '#C3423F', kde = True)
plt.tight_layout()
plt.savefig("binomial distribution.png")
plt.close()


#Part two of assignment - permuations
#Showing difference between shuffle and permuations
#Shuffle changes original array but permuation returns new array without altering existing one

def permutation_array (r):
    arr = np.arange(r)
    print(random.permutation(arr))
    return arr

arr = permutation_array(30)
print(arr)

def shuffle_array (a):
    random.shuffle(a)
    return a

newarr = shuffle_array(a = arr)
print(newarr)


