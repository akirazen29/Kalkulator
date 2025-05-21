def tambah (a, b):
	return a + b

def kurang (a, b):
	return a - b

def kali (a, b):
	return a * b
	
def bagi (a, b):
	return a / b
	
def modulus (a, b):
	return a % b
	
# tampilan menu
while True:
    print("====KALKULATOR RIBET====")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Modulus")
    print("0. Untuk Keluar")

    # input user
    pilihan = input("Pilih operasi (0-5): ")

    if pilihan == "0":
        print("Thanks Sudah Memakai Program Ini!!")
        break

    x = int(input("Masukan Angka Pertama: "))
    y = int(input("Masukan Angka Kedua: "))

    # proses dan output
    if pilihan == "1":
        print("Hasil = ", tambah(x, y))
    elif pilihan == "2":
        print("Hasil = ", kurang(x, y))
    elif pilihan == "3":
        print("Hasil = ", kali(x, y))
    elif pilihan == "4":
        print("Hasil = ", bagi(x, y))
    elif pilihan == "5":
        print("Hasil = ", modulus(x, y))
    else:
        print("Pilihan tidak valid.")