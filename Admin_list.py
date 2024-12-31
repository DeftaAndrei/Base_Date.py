import datetime as dt

class Member:
    '''The attributes and methods are for everyone'''

    expiry_days = 365

    def __init__(self, Nume, Prenume, Data_de_nastere=None, Oras=None, Skill_1=None, Skill_2=None):
        self.nume = Nume
        self.prenume = Prenume
        self.data_de_nastere = dt.datetime.strptime(Data_de_nastere, "%Y-%m-%d") if Data_de_nastere else None
        self.oras = Oras
        self.skill_1 = Skill_1
        self.skill_2 = Skill_2
        self.data_inregistrare = dt.datetime.now()
        self.data_expirare = self.data_inregistrare + dt.timedelta(days=self.expiry_days)

    def afiseaza_detalii(self):
        """Afișează detaliile membrului."""
        return (f"Membru: {self.nume} {self.prenume}\n"
                f"Locație: {self.oras}\n"
                f"Skill-uri: {self.skill_1}, {self.skill_2}\n"
                f"Data înregistrare: {self.data_inregistrare.strftime('%Y-%m-%d')}\n"
                f"Data expirare: {self.data_expirare.strftime('%Y-%m-%d')}")


class Admin(Member):
    """Clasa Admin extinde funcționalitatea Member."""
    
    ex_day = 365 * 100  # Valabilitate pe 100 de ani

    def __init__(self, Nume, Prenume, Secret_Code):
        super().__init__(Nume, Prenume)
        self.secret_code = Secret_Code
        self.data_expirare = self.data_inregistrare + dt.timedelta(days=self.ex_day)

    def afiseaza_detalii(self):
        """Afișează detalii pentru un admin."""
        return (super().afiseaza_detalii() + f"\nCod secret: {self.secret_code}")


class User(Admin):
    """Clasa User moștenește Admin."""
    pass


# Crearea unui obiect Admin
Defta= Admin('Defta', 'Andrei', 'Alcatraz2000@#')

# Afișarea detaliilor obiectului
print(Ann.afiseaza_detalii())
