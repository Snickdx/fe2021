
import csv
from main import app
from models import db, Product

db.create_all(app=app)




print('database initialized!')