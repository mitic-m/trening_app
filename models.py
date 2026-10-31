from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

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

    dani: Mapped[list["DanPlana"]] = relationship(
        back_populates="plan", order_by="DanPlana.redni_broj"
    )


class DanPlana(Base):
    __tablename__ = "dani_plana"

    id: Mapped[int] = mapped_column(primary_key=True)
    plan_id: Mapped[int] = mapped_column(ForeignKey("planovi.id"))
    naziv: Mapped[str] = mapped_column(String(100))
    redni_broj: Mapped[int]

    plan: Mapped["Plan"] = relationship(back_populates="dani")
    vezbe: Mapped[list["VezbaUDanu"]] = relationship(back_populates="dan")


class VezbaUDanu(Base):
    __tablename__ = "vezbe_u_danu"

    id: Mapped[int] = mapped_column(primary_key=True)
    dan_id: Mapped[int] = mapped_column(ForeignKey("dani_plana.id"))
    vezba_id: Mapped[int] = mapped_column(ForeignKey("vezbe.id"))
    serije: Mapped[int]
    ponavljanja: Mapped[int]

    dan: Mapped["DanPlana"] = relationship(back_populates="vezbe")
    vezba: Mapped["Vezba"] = relationship()

class Trening(Base):
    __tablename__ = "treninzi"

    id: Mapped[int] = mapped_column(primary_key=True)
    klijent_id: Mapped[int] = mapped_column(ForeignKey("klijenti.id"))
    dan_id: Mapped[int] = mapped_column(ForeignKey("dani_plana.id"))
    datum: Mapped[date] = mapped_column(Date)
    osecaj_pri_dolasku: Mapped[int]
    osecaj_tokom: Mapped[int]
    komentar: Mapped[str | None]
    serije: Mapped[list["SerijaTreninga"]] = relationship(
        back_populates="trening",
        order_by=lambda: [SerijaTreninga.vezba_id, SerijaTreninga.redni_broj],
    )


class SerijaTreninga(Base):
    __tablename__ = "serije_treninga"

    id: Mapped[int] = mapped_column(primary_key=True)
    trening_id: Mapped[int] = mapped_column(ForeignKey("treninzi.id"))
    vezba_id: Mapped[int] = mapped_column(ForeignKey("vezbe.id"))
    redni_broj: Mapped[int]
    kilaza: Mapped[float]
    ponavljanja: Mapped[int]
    trening: Mapped["Trening"] = relationship(back_populates="serije")
    vezba: Mapped["Vezba"] = relationship()