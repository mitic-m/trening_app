from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def pocetna():
    return {"poruka": "Aplikacija za trening radi!"}


@app.post("/klijenti", response_model=schemas.KlijentOut)
def dodaj_klijenta(podaci: schemas.KlijentCreate, db: Session = Depends(get_db)):
    klijent = models.Klijent(**podaci.model_dump())
    db.add(klijent)
    db.commit()
    db.refresh(klijent)
    return klijent


@app.get("/klijenti", response_model=list[schemas.KlijentOut])
def svi_klijenti(db: Session = Depends(get_db)):
    return db.query(models.Klijent).all()


@app.delete("/klijenti/{klijent_id}")
def obrisi_klijenta(klijent_id: int, db: Session = Depends(get_db)):
    klijent = db.get(models.Klijent, klijent_id)
    if klijent is None:
        raise HTTPException(status_code=404, detail="Klijent ne postoji")
    db.delete(klijent)
    db.commit()
    return {"poruka": "Klijent obrisan"}