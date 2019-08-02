import pytest
from app import create_app, db
from config import Config
from app.models import Chocolate, Wine

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://"

@pytest.fixture
def client():
    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()
    db.create_all()

    with app.test_client() as client:
        yield client

    db.session.remove()
    db.drop_all()
    app_context.pop()

@pytest.fixture
def sample_chocolate(client):
    chocolate = Chocolate(name = "Kit Kat")
    db.session.add(chocolate)
    db.session.commit()
    return chocolate

@pytest.fixture
def sample_wine(sample_chocolate):
    wine = Wine(name = "Syrah", chocolate = sample_chocolate)
    db.session.add(wine)
    db.session.commit()
    return wine

@pytest.fixture
def solo_wine(client):
    wine = Wine(name = "Chardonnay")
    db.session.add(wine)
    db.session.commit()
    return wine