class ATM:
    def __init__(self, saldo_awal):
        self.saldo = saldo_awal

    def cek_saldo(self):
        return self.saldo

    def tarik_tunai(self, jumlah_tarik):
        if jumlah_tarik > 0 and jumlah_tarik <= self.saldo:
            self.saldo -= jumlah_tarik
            return f"Penarikan berhasil. Sisa saldo: {self.saldo}"
        else:
            return "Penarikan gagal. Saldo tidak mencukupi."

    def setor_tunai(self, jumlah_setor):
        if jumlah_setor > 0:
            self.saldo += jumlah_setor
            return f"Setoran berhasil. Saldo sekarang: {self.saldo}"
        else:
            return "Setoran gagal. Jumlah setoran tidak valid."

def main():
    saldo_awal = 1000  # Ganti dengan saldo awal sesuai kebutuhan
    atm = ATM(saldo_awal)

    while True:
        print("\n=== ATM Sederhana ===")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            print(f"Saldo Anda saat ini: {atm.cek_saldo()}")
        elif pilihan == "2":
            jumlah_tarik = int(input("Masukkan jumlah penarikan: "))
            print(atm.tarik_tunai(jumlah_tarik))
        elif pilihan == "3":
            jumlah_setor = int(input("Masukkan jumlah setoran: "))
            print(atm.setor_tunai(jumlah_setor))
        elif pilihan == "4":
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()
