
import csv
from main import app
from models import db, Product

db.create_all(app=app)


with open('products.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        product = Product(
            name=row['Product Name'],
            category=row['Category'],
            price=float(row['Selling Price']),
            image=row['Image'],
            about=row['About Product']
        )
        db.session.add(product)
    db.session.commit()


print('database initialized!')