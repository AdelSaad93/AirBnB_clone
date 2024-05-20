from datetime import datetime
import models
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        # attributes initialization
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
    
    def to_dict(self):
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
