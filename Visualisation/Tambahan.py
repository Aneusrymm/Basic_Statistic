"""Title
Title atau judul merupakan salah satu komponen penting guna menyampaikan konteks pada sebuah visualisasi data.
Kita bisa menambahkan judul pada visualisasi data menggunakan function title() yang disediakan oleh matplotlib.

Label axes
Selain judul visualisasi, kita juga perlu menambahkan label atau keterangan pada setiap sumbu yang terdapat dalam visualisasi data.
Hal ini dilakukan untuk memberikan konteks terkait titik data yang direpresentasikan. 
Kita bisa membuat label axes menggunakan function xlabel() dan ylabel() yang disediakan oleh library matplotlib.

Legend
Pastikan Anda menambahkan legend memberikan keterangan untuk variabel yang tidak digambarkan pada sumbu. 
Keterangan yang digunakan akan bergantung pada cara kita dalam merepresentasikan variabel tambahan tersebut. 
Sebagai contoh, kita bisa menggunakan legend() untuk memberikan keterangan pada variabel kategoris tambahan. 
Namun, apabila variabel tambahan tersebut berupa nilai numerik yang direpresentasikan menggunakan range warna, 
kita bisa memanfaatkan function colorbar() untuk memberikan keterangan pada variabel tersebut.
"""
import pandas as pd
import matplotlib.pyplot as plt
 
url = 'https://query1.finance.yahoo.com/v7/finance/download/BBCA.JK?period1=1644796800&period2=1676332800&interval=1d&events=history&includeAdjustedClose=true'
df = pd.read_csv(url)
df['Date'] = pd.to_datetime(df['Date'])
 
plt.figure(figsize=(12, 5))
plt.plot(df['Date'], df['Close'], label='Close', color='red')
plt.plot(df['Date'], df['Open'], label='Open', color='blue')
plt.title('BBCA Stock Price', size=20)
plt.xlabel('Date',size=15)
plt.ylabel('Price (IDR)',size=15)
plt.legend()
plt.show()