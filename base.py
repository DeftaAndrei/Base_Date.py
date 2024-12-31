import datetime as dt

class Member:
    '''The attributes and methods are for everyone'''
    
    # By default, a new account expires in one year (365 days)
    expiry_days = 365

    def __init__(self, nume, prenume, data_de_nastere, oras, skill_1, skill_2):
        self.nume = nume
        self.prenume = prenume
        self.data_de_nastere = dt.datetime.strptime(data_de_nastere, "%Y-%m-%d")
        self.oras = oras
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.data_inregistrare = dt.datetime.now()  # Data curentă la înregistrare
        self.data_expirare = self.data_inregistrare + dt.timedelta(days=self.expiry_days)

    def calculeaza_varsta(self):
        """Returnează vârsta membrului."""
        azi = dt.datetime.now()
        return azi.year - self.data_de_nastere.year - (
            (azi.month, azi.day) < (self.data_de_nastere.month, self.data_de_nastere.day)
        )

    def extinde_abonamentul(self, zile):
        """Extinde data de expirare cu un anumit număr de zile."""
        self.data_expirare += dt.timedelta(days=zile)

    def afiseaza_detalii(self):
        """Afișează detaliile membrului."""
        return (f"Membru: {self.nume} {self.prenume}\n"
                f"Vârsta: {self.calculeaza_varsta()} ani\n"
                f"Locație: {self.oras}\n"
                f"Skill-uri: {self.skill_1}, {self.skill_2}\n"
                f"Data înregistrare: {self.data_inregistrare.strftime('%Y-%m-%d')}\n"
                f"Data expirare: {self.data_expirare.strftime('%Y-%m-%d')}")

# Exemplu de utilizare:
membru1 = Member(
    nume="Defta",
    prenume="Andrei",
    data_de_nastere="2000-08-19",
    oras="București",
    skill_1="Python",
    skill_2="Machine Learning"
)

print(membru1.afiseaza_detalii())
membru1.extinde_abonamentul(30)  
print(f"Noua dată de expirare: {membru1.data_expirare.strftime('%Y-%m-%d')}")
