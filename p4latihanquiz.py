# CLASS DAN OBJECT

class Taman:
    def __init__(self):
        self.nama = "Taman Kota"
        self.alamat = "Serang"


class Pengunjung:
    # Class Attribute
    tempat = "Taman Kota"

    # Constructor untuk data pengunjung
    def __init__(self, nama, kegiatan, umur, taman):
        self.nama = nama
        self.kegiatan = kegiatan
        self.umur = umur
        self.taman = taman

    # Method perkenalan
    def kenalan(self):
        print(f"Halo, nama saya {self.nama}.")
        print(f"Umur saya {self.umur} tahun.")
        print(f"Saya sedang {self.kegiatan}.")
        print(f"Saya berada di {self.taman}.")
        print("Senang bisa menikmati suasana taman.")

    # Method percakapan
    def hello(self, nama):
        print(f"Halo {nama}, perkenalkan nama saya {self.nama}.")
        print("Bagaimana kabar kamu hari ini?")
        print(f"Saya berumur {self.umur} tahun.")
        print("Senang bisa bertemu dengan teman baru.")

    # Method menampilkan kegiatan
    def kegiatan_pengunjung(self):
        print(f"Nama saya {self.nama}.")
        print(f"Saya sedang {self.kegiatan}.")
        print("Saya suka menghabiskan waktu di taman.")

    # Method percakapan antara dua pengunjung
    def percakapan(self, teman):

        print("===== PERCAKAPAN DI TAMAN =====")

        print(f"{self.nama}: Hai, selamat sore {teman.nama}.")
        print(f"{teman.nama}: Hai {self.nama}, selamat sore juga.")

        print(f"{self.nama}: Kamu sedang apa di taman?")
        print(f"{teman.nama}: Saya sedang duduk santai menikmati pemandangan.")

        print(f"{self.nama}: Tamannya sangat indah dan sejuk ya.")
        print(f"{teman.nama}: Iya, cocok sekali untuk bersantai.")

        print(f"{self.nama}: Bagaimana kalau kita jalan-jalan sebentar?")
        print(f"{teman.nama}: Boleh, sekalian menikmati udara segar.")

        print(f"{self.nama}: Setelah itu kita duduk di bangku taman.")
        print(f"{teman.nama}: Boleh juga, sambil bercerita.")

        print(f"{self.nama}: Senang bisa menghabiskan waktu bersama.")
        print(f"{teman.nama}: Iya, semoga kita bisa ke sini lagi.")


# Membuat object taman
taman1 = Taman()

# Membuat object pengunjung pertama
pengunjung1 = Pengunjung("Manda", "Jalan-jalan", 19, taman1.nama)

# Membuat object pengunjung kedua
pengunjung2 = Pengunjung("Ayu", "Duduk santai", 20, taman1.nama)


# Memanggil method perkenalan
print("===== PERKENALAN PENGUNJUNG =====")

pengunjung1.kenalan()
print()

pengunjung2.kenalan()
print()


# Memanggil method kegiatan
print("===== KEGIATAN PENGUNJUNG =====")

pengunjung1.kegiatan_pengunjung()
print()

pengunjung2.kegiatan_pengunjung()
print()


# Percakapan antara Manda dan Ayu
pengunjung1.percakapan(pengunjung2)