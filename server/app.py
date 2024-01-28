#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Home(Resource):
    def get(self):
        return jsonify({"message": "Welcome to the Plants API"})

class Plants(Resource):
    def get(self):
        plants = Plant.query.all()
        plants_list = [plant.to_dict() for plant in plants]
        return jsonify(plants_list)

    def post(self):
        
        new_plant = Plant(
            name=request.form['name'], 
            image=request.form['image'], 
            price=request.form['price'],
            )
        db.session.add(new_plant)
        db.session.commit()
        response_dict = new_plant.to_dict()
        response = make_response(
            jsonify(response_dict), 
            201,
        )

        return response 

class PlantByID(Resource):
    def get(self, id):
        plant = Plant.query.get(id)
        if plant:
            return jsonify(plant.to_dict())
        else:
            return jsonify({"error": "Plant not found"}), 404

api.add_resource(Home, '/')
api.add_resource(Plants, '/plants')
api.add_resource(PlantByID, '/plants/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
