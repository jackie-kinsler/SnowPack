"""Dropdb, createdb, and populate all tables"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb mapping')
os.system('createdb mapping')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/trails.json') as f:
    trail_data = json.loads(f.read())


# Create trails, store them in list

trails_in_db = []
for trail in trail_data:
    name = trail.get('name')
    desc = trail.get('summary')
    long = trail.get('longitude')
    lat = trail.get('latitude')
    kml = None 
    length = trail.get('length')
    ascent = trail.get('ascent')
    descent = trail.get('descent')
    difficulty = trail.get('difficulty')
    location = trail.get('location')
    url = trail.get('url')
    img = trail.get('imgMedium')
    
    
    trail = crud.create_movie(title, overview, release_date, poster_path)

    trails_in_db.append(trail)
 
# for n in range(10):
#     email = f'user{n}@test.com'
#     password = 'test'
#     user = crud.create_user(email, password)
    
#     for _ in range(10):
#         crud.create_rating(user, choice(movies_in_db), randint(1,5))
