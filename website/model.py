from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin
from sqlalchemy.dialects.mysql import CHAR, VARCHAR, DATE, DECIMAL, TEXT, INTEGER

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
    
class Product(db.Model):
    __tablename__ = 'product'

    code = db.Column(CHAR(10), primary_key=True)
    name = db.Column(VARCHAR(255), nullable=False)
    category = db.Column(VARCHAR(255), nullable=False)
    price = db.Column(DECIMAL(10, 2), nullable=False)
    quantity = db.Column(INTEGER, nullable=False)
    description = db.Column(TEXT, nullable=False)
    discount = db.Column(INTEGER, nullable=False)
    brand = db.Column(VARCHAR(255), nullable=False)
    review_rating = db.Column(DECIMAL(2, 1))
    review_count = db.Column(INTEGER, default=0)
    sold_count = db.Column(INTEGER, default=0)
    image_url = db.Column(VARCHAR(255))

    __table_args__ = (
        db.CheckConstraint('price > 0', name='check_price'),
        db.CheckConstraint('quantity >= 0', name='check_quantity'),
        db.CheckConstraint('discount >= 0 AND discount <= 99', name='check_discount'),
        db.CheckConstraint('review_rating >= 0 AND review_rating <= 5', name='check_review_rating'),
        db.CheckConstraint('review_count >= 0', name='check_review_count'),
        db.CheckConstraint('sold_count >= 0', name='check_sold_count'),
    )

    def __repr__(self):
        return f'<Product {self.name}>'