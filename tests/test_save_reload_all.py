#!/usr/bin/python3


# test_save_reload_all.py
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create new instances --")
my_state = State(name="California")
my_state.save()
print(my_state)

my_city = City(state_id=my_state.id, name="San Francisco")
my_city.save()
print(my_city)

my_amenity = Amenity(name="WiFi")
my_amenity.save()
print(my_amenity)

my_place = Place(city_id=my_city.id, user_id="", name="Lovely Place")
my_place.save()
print(my_place)

my_review = Review(place_id=my_place.id, user_id="", text="Great place!")
my_review.save()
print(my_review)
