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