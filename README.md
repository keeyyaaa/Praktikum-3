# praktikum 3-tipe data, variabel, dan operator 

nama: Ica Rizqiah

kelas: TI.24.A.5

NIM: 312410554

Mata Kuliah: Bahasa Pemograman


## Mencari bilangan terbesar dari bilangan yang diinputkan
Program ini menentukan bilangan terbesar dari serangkaian bilangan yang diinputkan hingga input 0. Program ini mneggunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar yang ditemukan.

## flowchart program
![foto](https://github.com/keeyyaaa/flowchart/blob/bd15ed17fc7d7d662e2d86405bc86cd7b17e967f/flowchart%20mj.jpg)

## kode program 
```python
MAX = int('0')

while True:
    x = int(input("Inputkan Bilangan x : "))
    if x == 0:
        break
    if x > MAX:
        MAX = x
print("Bilangan terbesar adalah :", MAX)

```

## penjelasan kode program
```python
MAX = int('0')  # Menginisialisasi variabel MAX dengan nilai 0, disini 0 diubah dari string ke integer
```
Pada baris ini, variabel `MAX` diinisialisasi dengan nilai 0. Ini digunakan untuk menyimpan nilai maksimum sementara dari bilangan yang akan diinput oleh pengguna.

```python
while True:  # Memulai loop tak terbatas yang hanya akan berhenti jika ada break
```
`while True`: adalah loop tak terbatas yang akan terus berulang sampai syarat untuk menghentikan loop (dengan `break`) terpenuhi.

```python
    x = int(input("Inputkan Bilangan x : "))  # Meminta input bilangan x dari pengguna
```
Pada setiap iterasi loop, program meminta pengguna untuk menginputkan bilangan. Input ini dikonversi dari string ke tipe data integer dan disimpan dalam variabel `x`.

```python
    if x == 0:  # Mengecek apakah bilangan yang diinput adalah 0
        break    # Jika ya, maka loop akan dihentikan (break)
```
Jika pengguna memasukkan angka 0, program akan menghentikan loop. Jadi, bilangan 0 digunakan sebagai penanda akhir input.

```python
    if x > MAX:  # Mengecek apakah bilangan x lebih besar dari nilai MAX
        MAX = x  # Jika ya, maka x menjadi nilai MAX yang baru
```
Jika bilangan yang diinput lebih besar daripada nilai `MAX` saat ini, maka nilai `MAX` diperbarui dengan bilangan baru tersebut.

```python
print("Bilangan terbesar adalah :", MAX)  # Mencetak nilai MAX setelah loop selesai


```
Setelah loop berhenti (ketika pengguna memasukkan 0), program mencetak bilangan terbesar yang telah disimpan dalam variabel `MAX`.

## hasil kode program 
![foto](https://github.com/keeyyaaa/flowchart/blob/bd15ed17fc7d7d662e2d86405bc86cd7b17e967f/Screenshot%202024-10-22%20122916.png)
