#program kategori ukuran
# Program menghitung luas persegi panjang dan menampilkan kategorinya
# meminta input dari pengguna
panjang=float(input("masukan panjang persegi panjang :"))
lebar=float(input("masukan lebar persegi panjang :"))
# menghitung luas
luas=panjang*lebar
#menampilkan hasil luas
print("luas persegi panjang :",luas)
# menentukan kategori ukuran berdasarkan luas
if luas<50:
    print("kategori kecil")
elif luas<=100:
    print("kategori sedang")
else:
    print("kategori besar")
