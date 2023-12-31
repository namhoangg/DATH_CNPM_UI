from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin
from sqlalchemy.dialects.mysql import CHAR, VARCHAR, DATE

class Buyer(db.Model, UserMixin):
    __tablename__ = 'buyer'

    ID = db.Column(CHAR(10), primary_key=True)
    Password = db.Column(VARCHAR(16), unique=True, nullable=False)
    Phone_number = db.Column(VARCHAR(10), unique=True, nullable=False)
    Address = db.Column(VARCHAR(60), nullable=False)
    Date_of_Birth = db.Column(DATE, nullable=False)
    Gender = db.Column(CHAR(1), nullable=False)
    First_Name = db.Column(VARCHAR(30), nullable=False)
    Last_Name = db.Column(VARCHAR(30), nullable=False)

    __table_args__ = (
        db.CheckConstraint('LENGTH(Phone_number) BETWEEN 9 AND 10', name='check_phone_length2'),
        db.CheckConstraint("Gender IN ('M', 'F')", name='check_gender2'),
    )

    def __repr__(self):
        return f'<Buyer {self.First_Name} {self.Last_Name}>'