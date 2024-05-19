import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    __class_dict = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            temp = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(temp, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                deserialized_objects = json.load(file)
                for key, value in deserialized_objects.items():
                    class_name = value['__class__']
                    self.__objects[key] = self.__class_dict[class_name](**value)
        except FileNotFoundError:
            pass
