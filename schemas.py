from datetime import date
from pydantic import BaseModel, ConfigDict


class KlijentCreate(BaseModel):
    ime: str
    prezime: str
    datum_rodjenja: date


class KlijentOut(KlijentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class VezbaCreate(BaseModel):
    naziv: str
    misicna_grupa: str | None = None


class VezbaOut(VezbaCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class PlanCreate(BaseModel):
    naziv: str
    klijent_id: int


class PlanOut(PlanCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class DanCreate(BaseModel):
    naziv: str
    redni_broj: int


class DanOut(DanCreate):
    id: int
    plan_id: int

    model_config = ConfigDict(from_attributes=True)


class VezbaUDanuCreate(BaseModel):
    vezba_id: int
    serije: int
    ponavljanja: int


class VezbaUDanuOut(VezbaUDanuCreate):
    id: int
    dan_id: int

    model_config = ConfigDict(from_attributes=True)