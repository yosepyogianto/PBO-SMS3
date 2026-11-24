class BankAccount:
    no = ""
    saldo = 0

    def __init__(self, no, saldo=0):
        self.no = no

        # Validasi saldo
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")

        self.saldo = saldo


Alfa = BankAccount("1234567890", 1000)  # sukses
Alex = BankAccount("1234567890", -1000)  # error