import matplotlib.pyplot as plt
import numpy as np
 
x = np.random.normal(15, 5, 250)
 
plt.hist(x=x, bins=15)
plt.show()

"""
x: menampung data yang akan divisualisasikan.
bins: menampung jumlah bins (sebanding dengan ukurannya) yang akan digunakan untuk membuat grafik histogr
"""

import seaborn as sns
 
sns.histplot(x=x, bins=15)
plt.show()