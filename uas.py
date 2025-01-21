import pandas as pd
import numpy as np
from tabulate import tabulate

# Membaca file excel
path = r"C:\Kuliah\SEMESTER 3\STATISTIK KOMPUTASI\UAS\bayes.xlsx"
df = pd.read_excel(path, skiprows=1)
bayes = pd.read_excel(path, skiprows=1)

table_title = "========= DATA TINGKAT KEPUASAN PENGGUNA GOOGLE CLASSROOM DALAM PEMBELAJARAN ONLINE ========="
print(f"\n{table_title}\n")

# Menampilkan data
table = tabulate(df.head(76), headers='keys', tablefmt='psql', showindex=False)
print(table)

attributes = ['sistem', 'layanan', 'informasi', 'penggunaan', 'pengguna']
values = ['ssetuju', 'setuju', 'tsetuju']
results = []

for attribute in attributes:
    for value in values:
        for hasil in ['Tidak Puas', 'Puas']:
            count = bayes.loc[(bayes[attribute] == value) & (bayes['hasil'] == hasil)].shape[0]
            results.append([attribute, value, hasil, count])

# Menghitung probabilitas masing-masing kolom
total_rows = len(df)

# Tabel sistem
bayes = df.head(75)
hasil = bayes["hasil"].head(75)
sistem = bayes["sistem"].head(75)

# Jumlah berdasarkn hasil Tidak puas
count_sistem_ssetuju_tidak_puas = bayes.loc[bayes['sistem'] == 'ssetuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
count_sistem_setuju_tidak_puas = bayes.loc[bayes['sistem'] == 'setuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
count_sistem_tsetuju_tidak_puas = bayes.loc[bayes['sistem'] == 'tsetuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
total_sistem_tidak_puas = count_sistem_ssetuju_tidak_puas+count_sistem_setuju_tidak_puas+count_sistem_tsetuju_tidak_puas

# Jumlah berdasarkn hasil Puas
count_sistem_ssetuju_puas = bayes.loc[bayes['sistem'] == 'ssetuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
count_sistem_setuju_puas = bayes.loc[bayes['sistem'] == 'setuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
count_sistem_tsetuju_puas = bayes.loc[bayes['sistem'] == 'tsetuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
total_sistem_puas = count_sistem_ssetuju_puas+count_sistem_setuju_puas+count_sistem_tsetuju_puas

# probabilitas sistem Tidak Puas
prob_count_sistem_ssetuju_tidak_puas = count_sistem_ssetuju_tidak_puas / total_sistem_tidak_puas
prob_count_sistem_setuju_tidak_puas = count_sistem_setuju_tidak_puas / total_sistem_tidak_puas
prob_count_sistem_tsetuju_tidak_puas = count_sistem_tsetuju_tidak_puas / total_sistem_tidak_puas
total_tidak_puas = prob_count_sistem_ssetuju_tidak_puas + prob_count_sistem_setuju_tidak_puas + prob_count_sistem_tsetuju_tidak_puas

# probabilitas sistem Puas
prob_count_sistem_ssetuju_puas = count_sistem_ssetuju_puas / total_sistem_puas
prob_count_sistem_setuju_puas = count_sistem_setuju_puas / total_sistem_puas
prob_count_sistem_tsetuju_puas = count_sistem_tsetuju_puas / total_sistem_puas
total_puas = prob_count_sistem_ssetuju_puas + prob_count_sistem_setuju_puas + prob_count_sistem_tsetuju_puas

# Menyusun data untuk tabel jumlah data
data_table = [
    ["ssetuju", count_sistem_ssetuju_puas, count_sistem_ssetuju_tidak_puas],
    ["setuju", count_sistem_setuju_puas, count_sistem_setuju_tidak_puas],
    ["tsetuju", count_sistem_tsetuju_puas, count_sistem_tsetuju_tidak_puas],
    ["Total", total_sistem_puas, total_sistem_tidak_puas,]
]

# Menampilkan tabel jumlah data
table_title = "==================================== TABEL SISTEM ======================================"
table_headers = ["Puas", "Tidak puas"]
print(f"\n{table_title}\n")
print(tabulate(data_table, headers=table_headers, tablefmt='plain'))

# Menyusun data untuk tabel
data_table = [
    ["ssetuju", round(prob_count_sistem_ssetuju_puas, 2), round(prob_count_sistem_ssetuju_tidak_puas, 2)], 
    ["setuju", round(prob_count_sistem_setuju_puas, 2), round(prob_count_sistem_setuju_tidak_puas, 2)],
    ["tsetuju", round(prob_count_sistem_tsetuju_puas, 2), round(prob_count_sistem_tsetuju_tidak_puas, 2)],
    ["Total", round(total_puas, 2), round(total_tidak_puas, 2)]
]

# Menampilkan tabel probabilitas
table_headers = ["Probabilitas Puas", "Probabilitas Tidak Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='psql'))


# Tabel layanan
bayes = df.head(75)
hasil = bayes["hasil"].head(75)
layanan = bayes["layanan"].head(75)

# Jumlah berdasarkn hasil Tidak puas
count_layanan_ssetuju_tidak_puas = bayes.loc[bayes['layanan'] == 'ssetuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
count_layanan_setuju_tidak_puas = bayes.loc[bayes['layanan'] == 'setuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
count_layanan_tsetuju_tidak_puas = bayes.loc[bayes['layanan'] == 'tsetuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
total_layanan_tidak_puas = count_layanan_ssetuju_tidak_puas+count_layanan_setuju_tidak_puas+count_layanan_tsetuju_tidak_puas

# Jumlah berdasarkn hasil Puas
count_layanan_ssetuju_puas = bayes.loc[bayes['layanan'] == 'ssetuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
count_layanan_setuju_puas = bayes.loc[bayes['layanan'] == 'setuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
count_layanan_tsetuju_puas = bayes.loc[bayes['layanan'] == 'tsetuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
total_layanan_puas = count_layanan_ssetuju_puas+count_layanan_setuju_puas+count_layanan_tsetuju_puas

# probabilitas layanan Tidak Puas
prob_count_layanan_ssetuju_tidak_puas = count_layanan_ssetuju_tidak_puas / total_layanan_tidak_puas
prob_count_layanan_setuju_tidak_puas = count_layanan_setuju_tidak_puas / total_layanan_tidak_puas
prob_count_layanan_tsetuju_tidak_puas = count_layanan_tsetuju_tidak_puas / total_layanan_tidak_puas
total_tidak_puas = prob_count_layanan_ssetuju_tidak_puas + prob_count_layanan_setuju_tidak_puas + prob_count_layanan_tsetuju_tidak_puas

# probabilitas layanan Puas
prob_count_layanan_ssetuju_puas = count_layanan_ssetuju_puas / total_layanan_puas
prob_count_layanan_setuju_puas = count_layanan_setuju_puas / total_layanan_puas
prob_count_layanan_tsetuju_puas = count_layanan_tsetuju_puas / total_layanan_puas
total_puas = prob_count_layanan_ssetuju_puas + prob_count_layanan_setuju_puas + prob_count_layanan_tsetuju_puas

# Menyusun data untuk tabel jumlah data
data_table = [
    ["ssetuju", count_layanan_ssetuju_puas, count_layanan_ssetuju_tidak_puas],
    ["setuju", count_layanan_setuju_puas, count_layanan_setuju_tidak_puas],
    ["tsetuju", count_layanan_tsetuju_puas, count_layanan_tsetuju_tidak_puas],
    ["Total", total_layanan_puas, total_layanan_tidak_puas,]
]

# Menampilkan tabel jumlah data
table_title = "==================================== TABEL LAYANAN ======================================"
table_headers = ["Puas", "Tidak puas"]
print(f"\n{table_title}\n")
print(tabulate(data_table, headers=table_headers, tablefmt='plain'))

# Menyusun data untuk tabel
data_table = [
    ["ssetuju", round(prob_count_layanan_ssetuju_puas, 2), round(prob_count_layanan_ssetuju_tidak_puas, 2)], 
    ["setuju", round(prob_count_layanan_setuju_puas, 2), round(prob_count_layanan_setuju_tidak_puas, 2)],
    ["tsetuju", round(prob_count_layanan_tsetuju_puas, 2), round(prob_count_layanan_tsetuju_tidak_puas, 2)],
    ["Total", round(total_puas, 2), round(total_tidak_puas, 2)]
]

# Menampilkan tabel probabilitas
table_headers = ["Probabilitas Puas", "Probabilitas Tidak Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='psql'))

# informasi
bayes = df.head(75)
hasil = bayes["hasil"]
informasi = bayes["informasi"]

# Jumlah berdasarkn hasil Tidak puas
count_informasi_ssetuju_tidak_puas = bayes.loc[bayes['informasi'] == 'ssetuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
count_informasi_setuju_tidak_puas = bayes.loc[bayes['informasi'] == 'setuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
count_informasi_tsetuju_tidak_puas = bayes.loc[bayes['informasi'] == 'tsetuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
total_informasi_tidak_puas = count_informasi_ssetuju_tidak_puas+count_informasi_setuju_tidak_puas+count_informasi_tsetuju_tidak_puas

# Jumlah berdasarkn hasil Puas
count_informasi_ssetuju_puas = bayes.loc[bayes['informasi'] == 'ssetuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
count_informasi_setuju_puas = bayes.loc[bayes['informasi'] == 'setuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
count_informasi_tsetuju_puas = bayes.loc[bayes['informasi'] == 'tsetuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
total_informasi_puas = count_informasi_ssetuju_puas+count_informasi_setuju_puas+count_informasi_tsetuju_puas

# probabilitas informasi Tidak Puas
prob_count_informasi_ssetuju_tidak_puas = count_informasi_ssetuju_tidak_puas / total_informasi_tidak_puas
prob_count_informasi_setuju_tidak_puas = count_informasi_setuju_tidak_puas / total_informasi_tidak_puas
prob_count_informasi_tsetuju_tidak_puas = count_informasi_tsetuju_tidak_puas / total_informasi_tidak_puas
total_tidak_puas = prob_count_informasi_ssetuju_tidak_puas + prob_count_informasi_setuju_tidak_puas + prob_count_informasi_tsetuju_tidak_puas

# probabilitas informasi Puas
prob_count_informasi_ssetuju_puas = count_informasi_ssetuju_puas / total_informasi_puas
prob_count_informasi_setuju_puas = count_informasi_setuju_puas / total_informasi_puas
prob_count_informasi_tsetuju_puas = count_informasi_tsetuju_puas / total_informasi_puas
total_puas = prob_count_informasi_ssetuju_puas + prob_count_informasi_setuju_puas + prob_count_informasi_tsetuju_puas

# Menyusun data untuk tabel jumlah data
data_table = [
    ["ssetuju", count_informasi_ssetuju_puas, count_informasi_ssetuju_tidak_puas],
    ["setuju", count_informasi_setuju_puas, count_informasi_setuju_tidak_puas],
    ["tsetuju", count_informasi_tsetuju_puas, count_informasi_tsetuju_tidak_puas],
    ["Total", total_informasi_puas, total_informasi_tidak_puas,]
]

# Menampilkan tabel jumlah data
table_title = "==================================== TABEL INFORMASI ======================================"
table_headers = ["Puas", "Tidak puas"]
print(f"\n{table_title}\n")
print(tabulate(data_table, headers=table_headers, tablefmt='plain'))

# Menyusun data untuk tabel
data_table = [
    ["ssetuju", round(prob_count_informasi_ssetuju_puas, 2), round(prob_count_informasi_ssetuju_tidak_puas, 2)], 
    ["setuju", round(prob_count_informasi_setuju_puas, 2), round(prob_count_informasi_setuju_tidak_puas, 2)],
    ["tsetuju", round(prob_count_informasi_tsetuju_puas, 2), round(prob_count_informasi_tsetuju_tidak_puas, 2)],
    ["Total", round(total_puas, 2), round(total_tidak_puas, 2)]
]

# Menampilkan tabel probabilitas
table_headers = ["Probabilitas Puas", "Probabilitas Tidak Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='psql'))

# penggunaan
bayes = df.head(75)
hasil = bayes["hasil"].head(75)
penggunaan = bayes["penggunaan"].head(75)

# Jumlah berdasarkn hasil Tidak puas
count_penggunaan_ssetuju_tidak_puas = bayes.loc[bayes['penggunaan'] == 'ssetuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
count_penggunaan_setuju_tidak_puas = bayes.loc[bayes['penggunaan'] == 'setuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
count_penggunaan_tsetuju_tidak_puas = bayes.loc[bayes['penggunaan'] == 'tsetuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
total_penggunaan_tidak_puas = count_penggunaan_ssetuju_tidak_puas+count_penggunaan_setuju_tidak_puas+count_penggunaan_tsetuju_tidak_puas

# Jumlah berdasarkn hasil Puas
count_penggunaan_ssetuju_puas = bayes.loc[bayes['penggunaan'] == 'ssetuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
count_penggunaan_setuju_puas = bayes.loc[bayes['penggunaan'] == 'setuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
count_penggunaan_tsetuju_puas = bayes.loc[bayes['penggunaan'] == 'tsetuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
total_penggunaan_puas = count_penggunaan_ssetuju_puas+count_penggunaan_setuju_puas+count_penggunaan_tsetuju_puas

# probabilitas penggunaan Tidak Puas
prob_count_penggunaan_ssetuju_tidak_puas = count_penggunaan_ssetuju_tidak_puas / total_penggunaan_tidak_puas
prob_count_penggunaan_setuju_tidak_puas = count_penggunaan_setuju_tidak_puas / total_penggunaan_tidak_puas
prob_count_penggunaan_tsetuju_tidak_puas = count_penggunaan_tsetuju_tidak_puas / total_penggunaan_tidak_puas
total_tidak_puas = prob_count_penggunaan_ssetuju_tidak_puas + prob_count_penggunaan_setuju_tidak_puas + prob_count_penggunaan_tsetuju_tidak_puas

# probabilitas penggunaan Puas
prob_count_penggunaan_ssetuju_puas = count_penggunaan_ssetuju_puas / total_penggunaan_puas
prob_count_penggunaan_setuju_puas = count_penggunaan_setuju_puas / total_penggunaan_puas
prob_count_penggunaan_tsetuju_puas = count_penggunaan_tsetuju_puas / total_penggunaan_puas
total_puas = prob_count_penggunaan_ssetuju_puas + prob_count_penggunaan_setuju_puas + prob_count_penggunaan_tsetuju_puas

# Menyusun data untuk tabel jumlah data
data_table = [
    ["ssetuju", count_penggunaan_ssetuju_puas, count_penggunaan_ssetuju_tidak_puas],
    ["setuju", count_penggunaan_setuju_puas, count_penggunaan_setuju_tidak_puas],
    ["tsetuju", count_penggunaan_tsetuju_puas, count_penggunaan_tsetuju_tidak_puas],
    ["Total", total_penggunaan_puas, total_penggunaan_tidak_puas,]
]

# Menampilkan tabel jumlah data
table_title = "==================================== TABEL PENGGUNAAN ======================================"
table_headers = ["Puas", "Tidak puas"]
print(f"\n{table_title}\n")
print(tabulate(data_table, headers=table_headers, tablefmt='plain'))

# Menyusun data untuk tabel
data_table = [
    ["ssetuju", round(prob_count_penggunaan_ssetuju_puas, 2), round(prob_count_penggunaan_ssetuju_tidak_puas, 2)], 
    ["setuju", round(prob_count_penggunaan_setuju_puas, 2), round(prob_count_penggunaan_setuju_tidak_puas, 2)],
    ["tsetuju", round(prob_count_penggunaan_tsetuju_puas, 2), round(prob_count_penggunaan_tsetuju_tidak_puas, 2)],
    ["Total", round(total_puas, 2), round(total_tidak_puas, 2)]
]

# Menampilkan tabel probabilitas
table_headers = ["Probabilitas Puas", "Probabilitas Tidak Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='psql'))

# pengguna
bayes = df.head(75)
hasil = bayes["hasil"].head(75)
pengguna = bayes["pengguna"].head(75)

# Jumlah berdasarkn hasil Tidak puas
count_pengguna_ssetuju_tidak_puas = bayes.loc[bayes['pengguna'] == 'ssetuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
count_pengguna_setuju_tidak_puas = bayes.loc[bayes['pengguna'] == 'setuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
count_pengguna_tsetuju_tidak_puas = bayes.loc[bayes['pengguna'] == 'tsetuju'].loc[bayes['hasil'] == 'Tidak Puas'].shape[0]
total_pengguna_tidak_puas = count_pengguna_ssetuju_tidak_puas+count_pengguna_setuju_tidak_puas+count_pengguna_tsetuju_tidak_puas

# Jumlah berdasarkn hasil Puas
count_pengguna_ssetuju_puas = bayes.loc[bayes['pengguna'] == 'ssetuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
count_pengguna_setuju_puas = bayes.loc[bayes['pengguna'] == 'setuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
count_pengguna_tsetuju_puas = bayes.loc[bayes['pengguna'] == 'tsetuju'].loc[bayes['hasil'] == 'Puas'].shape[0]
total_pengguna_puas = count_pengguna_ssetuju_puas+count_pengguna_setuju_puas+count_pengguna_tsetuju_puas

# probabilitas pengguna Tidak Puas
prob_count_pengguna_ssetuju_tidak_puas = count_pengguna_ssetuju_tidak_puas / total_pengguna_tidak_puas
prob_count_pengguna_setuju_tidak_puas = count_pengguna_setuju_tidak_puas / total_pengguna_tidak_puas
prob_count_pengguna_tsetuju_tidak_puas = count_pengguna_tsetuju_tidak_puas / total_pengguna_tidak_puas
total_tidak_puas = prob_count_pengguna_ssetuju_tidak_puas + prob_count_pengguna_setuju_tidak_puas + prob_count_pengguna_tsetuju_tidak_puas

# probabilitas pengguna Puas
prob_count_pengguna_ssetuju_puas = count_pengguna_ssetuju_puas / total_pengguna_puas
prob_count_pengguna_setuju_puas = count_pengguna_setuju_puas / total_pengguna_puas
prob_count_pengguna_tsetuju_puas = count_pengguna_tsetuju_puas / total_pengguna_puas
total_puas = prob_count_pengguna_ssetuju_puas + prob_count_pengguna_setuju_puas + prob_count_pengguna_tsetuju_puas

# Menyusun data untuk tabel jumlah data
data_table = [
    ["ssetuju", count_pengguna_ssetuju_puas, count_pengguna_ssetuju_tidak_puas],
    ["setuju", count_pengguna_setuju_puas, count_pengguna_setuju_tidak_puas],
    ["tsetuju", count_pengguna_tsetuju_puas, count_pengguna_tsetuju_tidak_puas],
    ["Total", total_pengguna_puas, total_pengguna_tidak_puas,]
]

# Menampilkan tabel jumlah data
table_title = "==================================== TABEL PENGGUNA ======================================"
table_headers = ["Puas", "Tidak puas"]
print(f"\n{table_title}\n")
print(tabulate(data_table, headers=table_headers, tablefmt='plain'))

# Menyusun data untuk tabel
data_table = [
    ["ssetuju", round(prob_count_pengguna_ssetuju_puas, 2), round(prob_count_pengguna_ssetuju_tidak_puas, 2)], 
    ["setuju", round(prob_count_pengguna_setuju_puas, 2), round(prob_count_pengguna_setuju_tidak_puas, 2)],
    ["tsetuju", round(prob_count_pengguna_tsetuju_puas, 2), round(prob_count_pengguna_tsetuju_tidak_puas, 2)],
    ["Total", round(total_puas, 2), round(total_tidak_puas, 2)]
]

# Menampilkan tabel probabilitas
table_headers = ["Probabilitas Puas", "Probabilitas Tidak Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='psql'))

# Menghitung probabilitas kelas target "Puas" dan "Tidak Puas"
prob_target_puas = df.loc[df['hasil'] == 'Puas'].shape[0] / total_rows
prob_target_tidak_puas = df.loc[df['hasil'] == 'Tidak Puas'].shape[0] / total_rows

# Menampilkan hasil probabilitas kelas target
table_title = "================= HASIL PROBABILITAS KELAS TARGET 'Puas' dan 'Tidak Puas' ================="
print(f"\n{table_title}\n")
table_headers = ["Kelas Target", "Probabilitas"]
data_table = [["Puas", round(prob_target_puas, 3)], ["Tidak Puas", round(prob_target_tidak_puas, 3)]]
print(tabulate(data_table, headers=table_headers, tablefmt='psql'))

table_title = "==================================== INPUT KUALITAS ======================================"
print(f"\n{table_title}")

table_title = "Masukkan ssetuju, setuju, tsetuju"
print(f"\n{table_title}\n")


# Kualitas sistem
sistem = input("Masukkan Kualitas sistem: ")
if sistem == "tsetuju":
  sistem_tidak_puas = prob_count_sistem_tsetuju_tidak_puas
  sistem_puas = prob_count_sistem_tsetuju_puas
elif sistem == "setuju":
  sistem_tidak_puas = prob_count_sistem_setuju_tidak_puas
  sistem_puas = prob_count_sistem_setuju_puas
else:
  sistem_tidak_puas = prob_count_sistem_ssetuju_tidak_puas
  sistem_puas = prob_count_sistem_ssetuju_puas

# Kualitas layanan
layanan = input("Masukkan Kualitas Layanan: ")
if layanan == "tsetuju":
  layanan_tidak_puas = prob_count_layanan_tsetuju_tidak_puas
  layanan_puas = prob_count_layanan_tsetuju_puas
elif layanan == "setuju":
  layanan_tidak_puas = prob_count_layanan_setuju_tidak_puas
  layanan_puas = prob_count_layanan_setuju_puas
else:
  layanan_tidak_puas = prob_count_layanan_ssetuju_tidak_puas
  layanan_puas = prob_count_layanan_ssetuju_puas

# Kualitas informasi
informasi = input("Masukkan Kualitas informasi: ")
if informasi == "tsetuju":
  informasi_tidak_puas = prob_count_informasi_tsetuju_tidak_puas
  informasi_puas = prob_count_informasi_tsetuju_puas
elif informasi == "setuju":
  informasi_tidak_puas = prob_count_informasi_setuju_tidak_puas
  informasi_puas = prob_count_informasi_setuju_puas
else:
  informasi_tidak_puas = prob_count_informasi_ssetuju_tidak_puas
  informasi_puas = prob_count_informasi_ssetuju_puas

# Kualitas penggunaan
penggunaan = input("Masukkan Kualitas Penggunaan: ")
if penggunaan == "tsetuju":
  penggunaan_tidak_puas = prob_count_penggunaan_tsetuju_tidak_puas
  penggunaan_puas = prob_count_penggunaan_tsetuju_puas
elif penggunaan == "setuju":
  penggunaan_tidak_puas = prob_count_penggunaan_setuju_tidak_puas
  penggunaan_puas = prob_count_penggunaan_setuju_puas
else:
  penggunaan_tidak_puas = prob_count_penggunaan_ssetuju_tidak_puas
  penggunaan_puas = prob_count_penggunaan_ssetuju_puas

# Kepuasan pengguna
pengguna = input("Masukkan Kepuasan Kualitas Pengguna: ")
if pengguna == "tsetuju":
  pengguna_tidak_puas = prob_count_pengguna_tsetuju_tidak_puas
  pengguna_puas = prob_count_pengguna_tsetuju_puas
elif pengguna == "setuju":
  pengguna_tidak_puas = prob_count_pengguna_setuju_tidak_puas
  pengguna_puas = prob_count_pengguna_setuju_puas
else:
  pengguna_tidak_puas = prob_count_pengguna_ssetuju_tidak_puas
  pengguna_puas = prob_count_pengguna_ssetuju_puas

# Menghitung probabilitas total
tidak_puas = sistem_tidak_puas * layanan_tidak_puas * informasi_tidak_puas * penggunaan_tidak_puas * pengguna_tidak_puas
puas = sistem_puas * layanan_puas * informasi_puas * penggunaan_puas * pengguna_puas

# Menentukan hasil
hasil = "Puas" if puas > tidak_puas else "Tidak Puas"

# Menampilkan hasil
print("\n==================================== HASIL ANALISIS ======================================\n")
print(f"Probabilitas Puas: {puas:.4f}")
print(f"Probabilitas Tidak Puas: {tidak_puas:.4f}")
print(f"Hasil: {hasil}")
