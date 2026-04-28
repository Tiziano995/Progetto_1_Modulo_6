# Progetto: Gestione Biblioteca Digitale

print('Benvenuti nel Database della biblioteca "Il Sapere":')

# ============================
# PARTE 1 – VARIABILI E TIPI DI DATI
# ============================

titolo_libro = "Assassinio sull'Orient Express"
numero_copie = 6
prezzo_medio = 13.99
disponibile = True

print("\nEsempio variabili:")
print("Titolo del libro:", titolo_libro)
print("Numero di copie disponibili:", numero_copie)
print("Prezzo medio:", prezzo_medio)
print("Disponibile:", disponibile)

# ============================
# PARTE 2 – STRUTTURE DATI
# ============================

lista_libri = [
    "Assassinio sull'Orient Express",
    "IT",
    "Il Miglio Verde",
    "Normal People",
    "Rancore"
]

dizionario_copie = {
    "Assassinio sull'Orient Express": 6,
    "IT": 4,
    "Il Miglio Verde": 2,
    "Normal People": 3,
    "Rancore": 10
}

set_utenti = {"Marco", "Carlo", "Francesca", "Antonio", "Emanuela"}

print("\nLista libri disponibili:")
print(lista_libri)

print("\nCopie disponibili per libro:")
for titolo, copie in dizionario_copie.items():
    print(f"- {titolo}: {copie} copie")

print("\nUtenti registrati:")
print(set_utenti)

# ============================
# PARTE 3 – CLASSI E OOP
# ============================

class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        return (
            f'Libro: "{self.titolo}" | Autore: {self.autore} | '
            f"Anno: {self.anno} | Copie disponibili: {self.copie_disponibili}"
        )


class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        return f"Utente: {self.nome} (età {self.eta}, ID: {self.id_utente})"


class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self):
        return (
            f'Prestito: {self.utente.nome} (ID: {self.utente.id_utente}) '
            f'ha preso "{self.libro.titolo}" per {self.giorni} giorni.'
        )

# ============================
# CREAZIONE OGGETTI (LIBRI E UTENTI)
# ============================

libri_oggetti = [
    Libro("Assassinio sull'Orient Express", "Agatha Christie", 1934, dizionario_copie["Assassinio sull'Orient Express"]),
    Libro("IT", "Stephen King", 1986, dizionario_copie["IT"]),
    Libro("Il Miglio Verde", "Stephen King", 1996, dizionario_copie["Il Miglio Verde"]),
    Libro("Normal People", "Sally Rooney", 2018, dizionario_copie["Normal People"]),
    Libro("Rancore", "Giancarlo Carofiglio", 2022, dizionario_copie["Rancore"]),
]

utenti_oggetti = [
    Utente("Marco", 26, "16458"),
    Utente("Carlo", 22, "18439"),
    Utente("Francesca", 29, "14859"),
    Utente("Antonio", 50, "06125"),
    Utente("Emanuela", 15, "20548")
]

print("\nInfo libri:")
for l in libri_oggetti:
    print("-", l.info())

print("\nSchede utenti:")
for u in utenti_oggetti:
    print("-", u.scheda())

# ============================
# PARTE 4 – FUNZIONALITÀ
# ============================

def presta_libro(utente, libro, giorni):
    if libro.copie_disponibili >= 1:
        libro.copie_disponibili -= 1
        nuovo_prestito = Prestito(utente, libro, giorni)
        return nuovo_prestito
    else:
        print(f'Errore: nessuna copia disponibile per "{libro.titolo}".')
        return None

prestiti = []

p1 = presta_libro(utenti_oggetti[0], libri_oggetti[0], 10)
if p1 is not None:
    prestiti.append(p1)

p2 = presta_libro(utenti_oggetti[1], libri_oggetti[1], 7)
if p2 is not None:
    prestiti.append(p2)

p3 = presta_libro(utenti_oggetti[2], libri_oggetti[2], 14)
if p3 is not None:
    prestiti.append(p3)

print("\nElenco aggiornato copie disponibili per ciascun libro:")
for l in libri_oggetti:
    print(f'- "{l.titolo}": {l.copie_disponibili} copie')

print("\nDettagli di ogni prestito effettuato:")
for p in prestiti:
    print("-", p.dettagli())
