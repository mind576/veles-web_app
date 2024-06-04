from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTable
from settings import *
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy import String, Date, ForeignKey,LargeBinary,Integer,Boolean
from datetime import date
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
import uuid


Base: DeclarativeMeta = declarative_base()

UUID_ID = uuid.UUID


class User(SQLAlchemyBaseUserTable[int], Base):
    """
    User table with obvious and visible fields and options.
    """
    __tablename__ = 'users_table'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fullName: Mapped[str] = mapped_column(String,nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True,nullable=False)
    phone: Mapped[str] = mapped_column(String,unique=True, nullable=False)
    picture: Mapped[str] = mapped_column(String)
    birthDate: Mapped[str] = mapped_column(Date,nullable=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self):
        return f" id={self.id} name= {self.fullName} "



class Employee(Base):
    """ User Extension ORM model:\n
    This model extends class User and helps to store additional data fields for storing Workers data  .

    """
    __tablename__ = 'employee'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users_table.id"))
    position: Mapped[Optional[str]] = mapped_column(String,nullable=True)
    obligations: Mapped[str] = mapped_column(String,nullable=True)
    type: Mapped[str] = mapped_column(String,nullable=True)
    
    def __repr__(self):
        return f"Employee_id={self.user_id}   position={self.position} "
    
    
    
class Company(Base):
    """ Company ORM model:
    -- This model helps to store Company item data fields .
    Args:
        Base (SQLAlchemy Base class): 
    Returns:
        Company ORM Model:
    """
    __tablename__ = 'company_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    director: Mapped[Optional[int]] = mapped_column(ForeignKey("users_table.id"),nullable=True) # How many directors may run business ??
    phone: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String)
    address: Mapped[Optional[str]] = mapped_column(String)
    location: Mapped[Optional[str]] = mapped_column(String)
    info: Mapped[Optional[str]] = mapped_column(String)
    type: Mapped[Optional[str]] = mapped_column(String)
    nameLegal: Mapped[Optional[str]] = mapped_column(String)
    INN: Mapped[Optional[str]] = mapped_column(String)
    KPP: Mapped[Optional[str]] = mapped_column(String)
    OGRN: Mapped[Optional[str]] = mapped_column(String)
    OKPO: Mapped[Optional[str]] = mapped_column(String)
    BIK: Mapped[Optional[str]] = mapped_column(String)
    BankName: Mapped[Optional[str]] = mapped_column(String)
    BankAddrss: Mapped[Optional[str]] = mapped_column(String)
    corrAccount: Mapped[Optional[str]] = mapped_column(String)
    def __repr__(self):
        return f"Company Name={self.name} company_id={self.id}"