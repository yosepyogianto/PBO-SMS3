class Mahasiswa :
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")

    def hello(self, nama):
        print(f"Halo {self.nama}, nama saya {nama}")

mahasiswa = Mahasiswa ()
mahasiswa.nama = "Yosep"
mahasiswa.perkenalan()
mahasiswa.hello("Yanto")