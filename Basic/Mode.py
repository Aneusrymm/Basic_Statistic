import numpy as np
from scipy import stats

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
modus_jumlah_kucing = stats.mode(jumlah_kucing)
print("Modus jumlah kucing:",modus_jumlah_kucing.mode[0])
