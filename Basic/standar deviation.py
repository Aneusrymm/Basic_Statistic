import numpy as np
import pandas as pd
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
jumlah_kucing_series = pd.Series(jumlah_kucing)
print(jumlah_kucing_series.std())