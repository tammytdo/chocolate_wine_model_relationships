from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(ConfigClass):

    app = Flask(__name__)

    app.config.from_object(ConfigClass)

    db.init_app(app)

    migrate.init_app(app, db)

    with app.app_context():

        ##   Chocolate CRUD    #####################

        @app.route("/chocolates", methods = ["GET"])
        def all_chocolates():
            chocolates = [chocolate.to_dict() for chocolate in Chocolate.query.all()]
            return jsonify(chocolates)

        @app.route("/chocolates/<int:id>")
        def one_chocolate(id):
            chocolate = Chocolate.query.get(id)
            return jsonify(chocolate.to_dict())

        @app.route("/chocolates", methods = ["POST"])
        def create_chocolate():
            chocolate_info = request.json or request.form
            chocolate = Chocolate(name = chocolate_info.get("name"))
            db.session.add(chocolate)
            db.session.commit()

            return jsonify(chocolate.to_dict())

        @app.route("/chocolates/<int:id>", methods = ["PUT"])
        def update_chocolate(id):
            chocolate_info = request.json or request.form
            chocolate_id = Chocolate.query.filter_by(id = id).update(chocolate_info)
            db.session.commit()
            return jsonify(chocolate_id)

        @app.route("/chocolates/<int:id>", methods = ["DELETE"])
        def delete_chocolate(id):
            chocolate = Chocolate.query.get(id)
            db.session.delete(chocolate)
            db.session.commit()
            return jsonify(id)

        @app.route("/chocolates/<string:name>", methods = ["GET"])
        def get_chocolate_by_name(name):
            """
            somehow this route is different than /chocolates/id
            Magical!
            """
            chocolate = Chocolate.query.filter_by(name = name).first()
            return jsonify(chocolate.to_dict())

        ##   Wine CRUD  #####################
        @app.route("/wines", methods = ["GET"])
        def all_wines():
            wines = [wine.to_dict() for wine in Wine.query.all()]
            return jsonify(wines)

        @app.route("/wines/<int:id>")
        def one_wine(id):
            wine = Wine.query.get(id)
            return jsonify(wine.to_dict())

        @app.route("/wines", methods = ["POST"])
        def create_wine():
            wine_info = request.json or request.form
            wine = Wine(
                name = wine_info.get("name"), chocolate_id = wine_info.get("chocolate")
            )
            db.session.add(wine)
            db.session.commit()

            return jsonify(wine.to_dict())

        @app.route("/wines/<int:id>", methods = ["DELETE"])
        def delete_wine(id):
            pass

        @app.route("/wines/<int:id>", methods = ["PUT"])
        def update_wine(id):
            pass

        @app.route("/chocolates/<int:id>/wines")
        def get_wines_in_chocolate(id):
            wines = [wine.to_dict() for wine in Chocolate.query.get(id).wines]
            return jsonify(wines)

        return app

from app.models import Chocolate, Wine