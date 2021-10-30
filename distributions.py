import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()

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
plt.show()
