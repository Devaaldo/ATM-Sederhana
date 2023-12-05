import sys
#mengimport modul sys yang dimana fungsinya itu nanti dibawah untuk mengehentikan codingan


# Atribut kelas ATM
class ATM:
    def __init__(self):
        self.balance = 0
        self.start()

    # Fungsi untuk memulai ATM
    def start(self):
        while True:
            print("\n\n1. Simpan Uang")
            print("2. Tarik Uang")
            print("3. Periksa Saldo")
            print("4. Keluar")

            option = input("Masukkan nomor opsi yang diinginkan : ")

            if option == "1":
                self.simpan_uang()
            elif option == "2":
                self.tarik_uang()
            elif option == "3":
                self.periksa_saldo()
            elif option == "4":
                self.Keluar()
            else:
                print("Invalid input, please try again.")

    # Fungsi untuk menambahkan saldo
    def simpan_uang(self):
        amount = int(input("Masukkan jumlah uang yang ingin anda simpan : "))
        self.balance += amount
        print(f"Simpan berhasil. Saldo anda adalah: {self.balance}")

    # Fungsi untuk mentarik saldo
    def tarik_uang(self):
        amount = int(input("Enter the amount of money you would like to withdraw: "))
        if amount > self.balance:
            print("Withdrawal failed. Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Your new balance is: {self.balance}")

    # Fungsi untuk memeriksa saldo
    def periksa_saldo(self):
        print(f"Your current balance is: {self.balance}")

    # Fungsi untuk keluar dari ATM
    def Keluar(self):
        print("Exiting ATM...")
        sys.exit()
        #sys.exit ini fungsi dari menghentikan code yang berulang dan bisa jg diganti dengan break

# Buat objek ATM dan jalankan
ATM()