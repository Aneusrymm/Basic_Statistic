import matplotlib.pyplot as plt
 
flavors = ('Chocolate', 'Vanilla', 'Macha', 'Others')
votes = (50, 20, 30, 10)
colors = ('#8B4513', '#FFF8DC', '#93C572', '#E67F0D')
explode = (0.1, 0, 0, 0)
 
plt.pie(
    x=votes,
    labels=flavors,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode
)
plt.show()
"""
x: menampung data yang akan divisualisasikan.
explode: menampung array atau list yang mengatur posisi tiap irisan lingkaran.
labels: sekumpulan string yang digunakan untuk memberi label pada tiap irisan lingkaran.
colors: sekumpulan warna yang akan digunakan pada tiap irisan lingkaran.
autopct: string yang digunakan untuk memberi numerik label pada tiap irisan lingkaran.
"""

plt.pie(
    x=votes,
    labels=flavors,
    colors=colors,
    wedgeprops = {'width': 0.4}
)
plt.show()