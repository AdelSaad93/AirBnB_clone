import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        from models import storage  # Local import to avoid circular dependency
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__
        }

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
