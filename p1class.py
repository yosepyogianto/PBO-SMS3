class Sekolah:
    pass

class Siswa:
    pass

Bapa_Yosep= Sekolah()
Yanto = Siswa()

print(type(Bapa_Yosep))
print(type(Yanto))



Sir_Yosep = Sekolah()
Bapa_Yanto = Siswa()


print(type(Sir_Yosep))
print(type(Bapa_Yanto))

Kepala_sekolah = Sekolah()
Kepala_sekolah.umur = 36
Kepala_sekolah.nama = "Sir_Valdo"

print(Kepala_sekolah.umur)
print(Kepala_sekolah.nama)

Orang_tua = Siswa()
Orang_tua.umur = 59
Orang_tua.nama = "Budi"

print(Orang_tua.umur)
print(Orang_tua.nama)