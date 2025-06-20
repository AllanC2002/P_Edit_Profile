from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DB UserProfile
class Type(Base):
    __tablename__ = 'Types'
    Id_type = Column(Integer, primary_key=True, autoincrement=True)
    Description = Column(String(50))

class Preference(Base):
    __tablename__ = 'Preferences'
    Id_preferences = Column(Integer, primary_key=True, autoincrement=True)
    Description = Column(String(50))

class Profile(Base):
    __tablename__ = 'Profile'
    Id_User = Column(Integer, primary_key=True)
    User_mail = Column(String(100), unique=True)
    Name = Column(String(100))
    Lastname = Column(String(100))
    Description = Column(String(255))
    Id_preferences = Column(Integer, ForeignKey("Preferences.Id_preferences"))
    Id_type = Column(Integer, ForeignKey("Types.Id_type"))
    Status_account = Column(Integer, CheckConstraint("Status_account IN (0, 1)"))
