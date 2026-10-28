from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Klijent(Base):
    __tablename__ = "klijenti"

    id: Mapped[int] = mapped_column(primary_key=True)
    ime: Mapped[str] = mapped_column(String(100))
    prezime: Mapped[str] = mapped_column(String(100))
    datum_rodjenja: Mapped[date] = mapped_column(Date)


class Vezba(Base):
    __tablename__ = "vezbe"

    id: Mapped[int] = mapped_column(primary_key=True)
    naziv: Mapped[str] = mapped_column(String(100), unique=True)
    misicna_grupa: Mapped[str | None] = mapped_column(String(50), default=None)


class Plan(Base):
    __tablename__ = "planovi"

    id: Mapped[int] = mapped_column(primary_key=True)
    naziv: Mapped[str] = mapped_column(String(100))
    klijent_id: Mapped[int] = mapped_column(ForeignKey("klijenti.id"))


class DanPlana(Base):
    __tablename__ = "dani_plana"

    id: Mapped[int] = mapped_column(primary_key=True)
    plan_id: Mapped[int] = mapped_column(ForeignKey("planovi.id"))
    naziv: Mapped[str] = mapped_column(String(100))
    redni_broj: Mapped[int]

