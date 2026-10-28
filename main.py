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


@app.post("/vezbe", response_model=schemas.VezbaOut)
def dodaj_vezbu(podaci: schemas.VezbaCreate, db: Session = Depends(get_db)):
    postoji = db.query(models.Vezba).filter(models.Vezba.naziv == podaci.naziv).first()
    if postoji:
        raise HTTPException(status_code=400, detail="Vežba sa tim nazivom već postoji")
    vezba = models.Vezba(**podaci.model_dump())
    db.add(vezba)
    db.commit()
    db.refresh(vezba)
    return vezba


@app.get("/vezbe", response_model=list[schemas.VezbaOut])
def sve_vezbe(db: Session = Depends(get_db)):
    return db.query(models.Vezba).all()


@app.delete("/vezbe/{vezba_id}")
def obrisi_vezbu(vezba_id: int, db: Session = Depends(get_db)):
    vezba = db.get(models.Vezba, vezba_id)
    if vezba is None:
        raise HTTPException(status_code=404, detail="Vežba ne postoji")
    db.delete(vezba)
    db.commit()
    return {"poruka": "Vežba obrisana"}


@app.post("/planovi", response_model=schemas.PlanOut)
def dodaj_plan(podaci: schemas.PlanCreate, db: Session = Depends(get_db)):
    klijent = db.get(models.Klijent, podaci.klijent_id)
    if klijent is None:
        raise HTTPException(status_code=404, detail="Klijent ne postoji")
    plan = models.Plan(**podaci.model_dump())
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan


@app.get("/planovi", response_model=list[schemas.PlanOut])
def svi_planovi(db: Session = Depends(get_db)):
    return db.query(models.Plan).all()


@app.get("/klijenti/{klijent_id}/planovi", response_model=list[schemas.PlanOut])
def planovi_klijenta(klijent_id: int, db: Session = Depends(get_db)):
    return db.query(models.Plan).filter(models.Plan.klijent_id == klijent_id).all()


@app.post("/planovi/{plan_id}/dani", response_model=schemas.DanOut)
def dodaj_dan(plan_id: int, podaci: schemas.DanCreate, db: Session = Depends(get_db)):
    plan = db.get(models.Plan, plan_id)
    if plan is None:
        raise HTTPException(status_code=404, detail="Plan ne postoji")
    dan = models.DanPlana(plan_id=plan_id, **podaci.model_dump())
    db.add(dan)
    db.commit()
    db.refresh(dan)
    return dan


@app.get("/planovi/{plan_id}/dani", response_model=list[schemas.DanOut])
def dani_plana(plan_id: int, db: Session = Depends(get_db)):
    return (
        db.query(models.DanPlana)
        .filter(models.DanPlana.plan_id == plan_id)
        .order_by(models.DanPlana.redni_broj)
        .all()
    )


@app.post("/dani/{dan_id}/vezbe", response_model=schemas.VezbaUDanuOut)
def dodaj_vezbu_u_dan(dan_id: int, podaci: schemas.VezbaUDanuCreate, db: Session = Depends(get_db)):
    if db.get(models.DanPlana, dan_id) is None:
        raise HTTPException(status_code=404, detail="Dan ne postoji")
    if db.get(models.Vezba, podaci.vezba_id) is None:
        raise HTTPException(status_code=404, detail="Vežba ne postoji")
    stavka = models.VezbaUDanu(dan_id=dan_id, **podaci.model_dump())
    db.add(stavka)
    db.commit()
    db.refresh(stavka)
    return stavka


@app.get("/dani/{dan_id}/vezbe", response_model=list[schemas.VezbaUDanuOut])
def vezbe_u_danu(dan_id: int, db: Session = Depends(get_db)):
    return db.query(models.VezbaUDanu).filter(models.VezbaUDanu.dan_id == dan_id).all()