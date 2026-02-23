#EXPLORATORY DATA ANALYSIS (EDA) PADA DATA PENJUALAN SWALAYAN
#Implementasi Data Science

import pandas as pd
import matplotlib.pyplot as plt

#===================
# memuat data
#===================    

df = pd.read_csv('data_penjualan_swalayan.csv')

print("====INFO DATA====")
print(df.info())    

print("\n====5 DATA TERATAS====")
print(df.head())

#============================
# ringkasan statistik data
#============================
print("\n====RINGKASAN STATISTIK====")
print(df.describe())

if 'total_penjualan' not in df.columns:
    df['total_penjualan'] = df['jumlah'] * df['harga_satuan']

#============================
# histogram jumlah penjualan
#============================

plt.figure()
plt.hist(df['jumlah'], bins=10)
plt.title('Histogram Jumlah Penjualan')
plt.xlabel('Jumlah')
plt.ylabel('Frekuensi')
plt.show()  

#============================
# histogram harga satuan
#============================
plt.figure()
plt.hist(df['harga_satuan'], bins=10)
plt.title('Histogram Harga Satuan')
plt.xlabel('Harga Satuan')
plt.ylabel('Frekuensi')
plt.show()

#===========================================  
# scatter plot jumlah vs total penjualan
#===========================================
plt.figure()
plt.scatter(df['jumlah'], df['total_penjualan'])
plt.title('Scatter Plot Jumlah vs Total Penjualan') 
plt.xlabel('Jumlah')
plt.ylabel('Total Penjualan')
plt.show()

#===========================================
# bar chart produk terlaris
#===========================================
produk_terlaris = df.groupby('nama_produk')['jumlah'].sum().sort_values(ascending=False)

plt.figure()    
produk_terlaris.plot(kind='bar')
plt.title('Produk Terlaris')
plt.xlabel('Produk')
plt.ylabel('Total Terjual')
plt.xticks(rotation=45)
plt.show()
  
print("\nProduk paling laris:")
print(produk_terlaris.head(1))  