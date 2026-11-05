# Aplikacija za trening

Web aplikacija za trenera: vođenje klijenata, planova treninga i beleženje odrađenih treninga. Pravim je za sopstveni rad sa klijentima, a ujedno kao projekat za učenje backend razvoja.

## Šta radi

- Klijenti: dodavanje, izmena, brisanje
- Katalog vežbi
- Planovi treninga: dani, vežbe u danu, serije i ponavljanja
- Kopiranje plana drugom klijentu
- Beleženje treninga: kilaža i ponavljanja po seriji, osećaj pri dolasku i tokom treninga, komentar
- Istorija klijenta po vežbi (šta je radio prošli put)
- PDF plana za klijenta
- Jednostavan frontend: unos treninga, istorija treninga, pravljenje planova

## Tehnologije

- Python, FastAPI
- SQLAlchemy, SQLite
- Pydantic
- fpdf2 (PDF)
- HTML i JavaScript (frontend, odvojen od backenda)

## Pokretanje

1. Napravi virtuelno okruženje i instaliraj biblioteke:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Pokreni server iz glavnog foldera projekta:
   ```
   uvicorn main:app --reload
   ```
3. Otvori u browseru:
   - `http://127.0.0.1:8000/app/` za aplikaciju
   - `http://127.0.0.1:8000/docs` za dokumentaciju API-ja

Baza (`trening.db`) se pravi sama pri prvom pokretanju.

## Struktura

- `main.py`: API endpointi
- `models.py`: tabele u bazi
- `schemas.py`: šta API prima i vraća
- `database.py`: veza sa bazom
- `pdf_izvestaj.py`: pravljenje PDF-a
- `frontend/`: stranice u browseru
- `docs/zahtevi.md`: zahtevi i plan razvoja

## Napomene

- PDF koristi font Arial sa Windows računara (`C:\Windows\Fonts`), pa na drugom sistemu treba promeniti putanju fonta u `pdf_izvestaj.py`.
- Aplikacija je u aktivnom razvoju.