Alat za trenera za vođenje klijenata; ujedno projekat za učenje backend-a.

## Korisnici
- V1: samo trener
- V2: klijent (pregled planova i istorije, samo čitanje)

## V1, mora da ima
- Klijenti: profil (za sada samo ime, prezime i datum rođenja; ostalo kasnije)
- Vežbe: baza vežbi
- Plan treninga: dani -> vežbe -> serije/ponavljanja
- Šta se radi danas: prikaz treninga za izabrani dan
- Beleženje treninga: kilaža, broj ponavljanja i serija po vežbi
- Subjektivni osećaj: kako je došao na trening, kako se osećao tokom treninga
- Podaci se čuvaju u SQLite bazi

## Kasnije (V2+)
- Prijava i pregled za klijente (web, telefon)
- PDF izveštaj za klijenta
- Automatsko predlaganje plana na osnovu prethodnih treninga

## Nije u V1
- Prava mobilna aplikacija
- Plaćanja, prodaja drugima

## Tehnologije (okvirno)
- Backend: Python (FastAPI / Django / Flask, još biram)
- Frontend: Vue (kasnije)
- Baza: SQLite