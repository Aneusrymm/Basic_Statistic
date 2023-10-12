import matplotlib.pyplot as plt

cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta', 
          'Surakarta','Surabaya', 'Medan', 'Makassar')

populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               3481, 287750, 785409)


plt.bar(x=cities, height=populations)
plt.xticks(rotation=45)
plt.show()

# Bisa juga menggunakan kode di bawah ini untuk menanplikan grafik
"""
plt.barh(y=cities, width=populations)
plt.show()
"""
import pandas as pd
 
df = pd.DataFrame({
    'Cities': cities,
    'Population': populations,
})
 
df.sort_values(by='Population', inplace=True)
 
plt.barh(y=df["Cities"], width=df["Population"])
plt.show()

plt.barh(y=df["Cities"], width=df["Population"])
plt.xlabel("Population (Millions)")
plt.title("Population of Cities in Indonesia")
plt.show()
import seaborn as sns
 
sns.barplot(y=df["Cities"], x=df["Population"], orient="h", color='black')
plt.xlabel("Population (Millions)")
plt.title("Population of Cities in Indonesia")
plt.show()