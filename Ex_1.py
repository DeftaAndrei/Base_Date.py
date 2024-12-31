import datetime as dt
class Member:
    def __init__(self, username, nume, prenume):
        self.username = username
        self.nume = nume
        self.prenume = prenume
        self.date__joined= dt.date.today()
        self.is_active = True

# Inițializare corectă a obiectului cu toate cele trei argumente
New_Guy = Member("Defta", "Andrei", "Robert")

# Afișarea datelor membrului
print(f"Acestea sunt datele : {New_Guy.__dict__}\n")
print(f"Username: {New_Guy.username}\n")
print(f"Prenume: {New_Guy.prenume}\n")
print(f"Numele de familie: {New_Guy.nume}\n")
