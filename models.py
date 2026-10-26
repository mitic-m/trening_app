from datetime import date
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Klijent(Base):
    __tablename__ = "klijenti"

    id: Mapped[int] = mapped_column(primary_key=True)
    ime: Mapped[str] = mapped_column(String(100))
    prezime: Mapped[str] = mapped_column(String(100))
    datum_rodjenja: Mapped[date] = mapped_column(Date)