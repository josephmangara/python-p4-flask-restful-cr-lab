#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():

    Plant.query.delete()

    aloe = Plant(
        id=1,
        name="Aloe",
        image="https://i.pinimg.com/236x/07/95/94/079594f8aa485447059bc63e9ea65649.jpg",
        price=11.50,
    )

    zz_plant = Plant(
        id=2,
        name="ZZ Plant",
        image="https://i.pinimg.com/236x/8f/90/73/8f9073c850d592368f59280e512a64e1.jpg",
        price=25.98,
    )

    db.session.add_all([aloe, zz_plant])
    db.session.commit()
