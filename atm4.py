class ATM:
    def __init__(self, saldo_awal):
        self.saldo = saldo_awal

    def simpan_uang(self, jumlah_setor):
        if jumlah_setor > 0 :
            self.saldo += jumlah_setor
            return f"Simpan berhasil. Saldo anda adalah : {self.saldo}"
        else:
            return "Setoran gagal. Jumlah setoran tidak valid."
    
    def tarik_uang(self, jumlah_tarik):
        if jumlah_tarik > 0 and jumlah_tarik <= self.saldo:
            self.saldo -= jumlah_tarik
            return f"Penarikan berhasil. Sisa saldo: {self.saldo}"
        else:
            return "Penarikan gagal. Anda terlalu miskin."
    
    def cek_saldo(self):
        return self.saldo

def main():
    saldo_awal = 0
    atm = ATM(saldo_awal)

    while True:
        print("======================")
        print("     ATM REGAJAYA    ")
        print("======================")
        print("1. Simpan Uang")
        print("2. Tarik Uang")
        print("3. Cek Saldo")
        print("4. Cancel")


        pilihan = input("Masukkan nomor opsi yang diinginkan : ")

        if pilihan == "1":
            jumlah_setor = int(input("Masukkan jumlah uang yang ingin anda simpan :  "))
            print(atm.simpan_uang(jumlah_setor))
        elif pilihan == "2":
            jumlah_tarik = int(input("Masukkan jumlah penarikan: "))
            print(atm.tarik_uang(jumlah_tarik))
        elif pilihan == "3":
            print(f"Duit anda sekarang adalah : {atm.cek_saldo()}")
        elif pilihan == "4":
            print("Keluar dari ATM...")
            break
        else:
            print("Pilihan anda tidak valid. Silahkan pilih opsi 1, 2 , 3, atau 4.")

if __name__ == "__main__":
    main()