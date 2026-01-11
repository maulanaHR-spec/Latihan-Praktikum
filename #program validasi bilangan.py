#program validasi bilangan
#program untuk memeriksa apakah bilangan lebih besar dari 100 dan genap
#meminta input dari pengguna
bilangan=int(input("masukan sebuah bilangan :"))
#mengecek kondisi
if bilangan > 100 and bilangan % 2 == 0:
    print("bilangan lebih besar dari 100 dan merupakan bilangan genap")
else:
    print("bilangan tidak memenuhi kedua syarat")

