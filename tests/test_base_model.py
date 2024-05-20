import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
    
    def test_save_method(self):
        obj = BaseModel()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)
    
    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
