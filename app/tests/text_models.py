from app import db
from app.models import Chocolate, Wine

def test_chocolate(client):
    chocolate = Chocolate(name="Snickers")
    db.session.add(chocolate)
    db.session.commit()
    assert Chocolate.query.first().name == "Snickers"

def test_wine(client):
    wine = Wine(name="Reisling")
    db.session.add(wine)
    db.session.commit()
    assert Wine.query.first().name == "Reisling"

def test_wine_in_chocolate(client):
    chocolate = Chocolate(name="M&Ms")
    wine = Wine(name="Pinot Noir", chocolate=chocolate)
    db.session.add(wine)
    db.session.commit()
    assert Chocolate.query.first().name == "M&Ms"
    assert Wine.query.first().name == "Pinot Noir"
    
    wines_in_chocolate = Chocolate.query.first().wines
    assert wines_in_chocolate[0].name == "Pinot Noir"
    assert wines_in_chocolate[0].chocolate.name == "M&Ms"