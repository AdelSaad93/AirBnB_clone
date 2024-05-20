#!/usr/bin/python3


from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
            setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
            elif key != '__class__':
                   setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()
