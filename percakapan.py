# PERCAKAPAN PYTHON: YOSEP & AJIS
# Topik: Tanya Mata Kuliah & Jam Masuk Kuliah
def percakapan_kuliah():
    print("       SIMULASI CHAT: YOSEP & AJIS (KULIAH)       ")
    print("\nYosep : Halo Jis, lu masuk kuliah jam berapa hari ini?")
    jam_masuk = input("Ajis  ")
    print(f"\nYosep : Oh jam {jam_masuk}. Btw, hari ini kita ada mata kuliah apa aja ya?")
    mata_kuliah = input("Ajis  ")
    print(f"\nYosep : Wah matkul {mata_kuliah} ya. Masuknya di ruangan mana atau dosen siapa?")
    info_tambahan = input("Ajis : ")
    print("              RANGKUMAN JADWAL HARI INI            ")
    print(f"Jam Masuk Kuliah : {jam_masuk}")
    print(f"Mata Kuliah      : {mata_kuliah}")
    print(f"Info Tambahan    : {info_tambahan}")
    print("Yosep : Oke deh Jis infonya, makasih ya! Gas berangkat bareng?")
    print("Ajis  : Siap Yosep, gaslah!")
if __name__ == "__main__":
    percakapan_kuliah()