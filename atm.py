import sys

class ATM:
    def __init__(self):
        self.saku = 0
        self.start()

    def start(self):
        while True:
            print("\n\n1. Simpan Uang")
            print("2. Tarik Uang")
            print("3. Periksa Saldo")
            print("4. Keluar")

            option = int(input("Masukkan nomor opsi yang diinginkan : "))

            if option == 1:
                self.simpan_uang()
            elif option == 2:
                self.tarik_uang()
            elif option == 3:
                self.periksa_saldo()
            elif option == 4:
                self.keluar()
            else:
                print("Maaf opsi yang anda masukkan salah, tolong coba lagi.")

    def simpan_uang(self):
        jumlah = int(input("Masukkan jumlah uang yang ingin anda simpan : "))
        self.saku += jumlah
        print(f"Simpan berhasil. Saldo anda adalah : {self.saku}")
    
    def tarik_uang(self):
        jumlah = int(input(f"Masukkan jumlah uang yang mau anda tarik : "))
        if jumlah > self.saku:
            print("Tarik uang gagal. Anda miskin.")
        else:
            self.saku -= jumlah
            print(f"Tarik uang berhasil. Uang anda sekarang adalah : {self.saku} ")
    
    def periksa_saldo(self):
        print(f"Duit anda sekarang adalah : {self.saku}")
    
    def keluar(self):
        print("Keluar dari ATM...")
        sys.exit()
    
ATM()