# Progetto: Gestione Biblioteca Digitale

## Descrizione
Questo progetto simula un piccolo sistema software per la gestione di una biblioteca digitale.
L’obiettivo è mettere in pratica i concetti base di Python (variabili, strutture dati, strutture di controllo)
e soprattutto la programmazione orientata agli oggetti (OOP).

Il programma gestisce:
- libri disponibili
- utenti registrati
- prestiti effettuati

---

## Traccia
In una biblioteca digitale si vuole realizzare un piccolo sistema software per gestire libri, utenti e prestiti.
Il programma deve sfruttare variabili, tipi di dati, strutture di controllo e soprattutto la programmazione orientata agli oggetti (OOP).

---

## Consegna

### Parte 1 – Variabili e tipi di dati
Dichiarare e stampare alcune variabili di esempio:
- Titolo di un libro (stringa)
- Numero di copie disponibili (intero)
- Prezzo medio di un libro (float)
- Stato "disponibile/non disponibile" (booleano)

(Esempio: titolo = "Il Signore degli Anelli", copie = 5, ecc.)

---

### Parte 2 – Strutture dati
Creare:
- una lista con almeno 5 titoli di libri
- un dizionario che mappi il titolo del libro al numero di copie disponibili
- un insieme (set) che contenga tutti gli utenti registrati alla biblioteca

---

### Parte 3 – Classi e OOP
Creare le seguenti classi:

#### Classe `Libro`
Attributi:
- titolo
- autore
- anno
- copie_disponibili

Metodo:
- `info()` che restituisce una stringa descrittiva del libro

#### Classe `Utente`
Attributi:
- nome
- eta
- id_utente

Metodo:
- `scheda()` che stampa i dati dell’utente

#### Classe `Prestito`
Contiene:
- utente (oggetto Utente)
- libro (oggetto Libro)
- giorni (numero di giorni del prestito)

Metodo:
- `dettagli()` che stampa tutte le informazioni sul prestito

---

### Parte 4 – Funzionalità
Creare una funzione `presta_libro(utente, libro, giorni)` che:
- verifichi se il libro ha almeno 1 copia disponibile
  - se sì: riduca il numero di copie e crei un nuovo oggetto `Prestito`
  - se no: stampi un messaggio di errore

Simulare almeno 3 prestiti con utenti e libri diversi.

Stampare a video:
- l’elenco aggiornato delle copie disponibili per ciascun libro
- i dettagli di ogni prestito effettuato

---

## Risultato finale atteso
Alla fine dell’esecuzione, il programma mostra:
- le copie aggiornate per ogni libro dopo i prestiti
- i dettagli di ogni prestito effettuato (utente, libro, giorni)
- eventuali errori se un libro non ha copie disponibili
