from datetime import date
from pydantic import BaseModel, ConfigDict, Field


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


class VezbaUDanuDetalj(BaseModel):
    id: int
    serije: int
    ponavljanja: int
    vezba: VezbaOut

    model_config = ConfigDict(from_attributes=True)


class DanDetalj(BaseModel):
    id: int
    naziv: str
    redni_broj: int
    vezbe: list[VezbaUDanuDetalj]

    model_config = ConfigDict(from_attributes=True)


class PlanDetalj(BaseModel):
    id: int
    naziv: str
    klijent_id: int
    dani: list[DanDetalj]

    model_config = ConfigDict(from_attributes=True)


class TreningCreate(BaseModel):
    klijent_id: int
    dan_id: int
    datum: date
    osecaj_pri_dolasku: int = Field(ge=1, le=5)
    osecaj_tokom: int = Field(ge=1, le=5)
    komentar: str | None = None


class TreningOut(TreningCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SerijaCreate(BaseModel):
    vezba_id: int
    redni_broj: int
    kilaza: float
    ponavljanja: int


class SerijaOut(SerijaCreate):
    id: int
    trening_id: int

    model_config = ConfigDict(from_attributes=True)
