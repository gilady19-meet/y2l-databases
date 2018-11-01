from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def addproduct(name , price , haveit , quantity):
	product_object = Product(name=name, price=price, haveit=haveit , quantity=quantity)
	session.add(product_object)
	session.commit()


#def create_product():
  #TODO: complete the functions (you will need to change the function's inputs)
 # pass

def updateproduct(name , price , haveit):
	product_object = session.query(Product).filter_by(name=name).first()
	product_object.haveit=haveit
	if price<=300:
		product_object.price=price
	else:
		print("the price is too high!")
	session.commit()


def deleteproduct(id):
	session.query(Product).filter_by(id=id).delete()
	session.commit()


def get_product(id):
	pass  


# addproduct("shirt" , 100 , True , 50)
deleteproduct(2)
updateproduct("shirt" , 340, False)