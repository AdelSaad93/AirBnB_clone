import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj_key = "BaseModel." + self.obj.id

    def tearDown(self):
        """Remove the JSON file created during tests"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all(self):
        """Test that all() returns the correct dictionary of objects"""
        self.storage.new(self.obj)
        self.assertIn(self.obj_key, self.storage.all())
        self.assertEqual(self.storage.all()[self.obj_key], self.obj)

    def test_new(self):
        """Test that new() adds an object to the storage"""
        self.storage.new(self.obj)
        self.assertIn(self.obj_key, self.storage.all())
        self.assertEqual(self.storage.all()[self.obj_key], self.obj)

    def test_save(self):
        """Test that save() correctly serializes objects to file"""
        self.storage.new(self.obj)
        self.storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
            self.assertIn(self.obj_key, data)
            self.assertEqual(data[self.obj_key]["id"], self.obj.id)

    def test_reload(self):
        """Test that reload() correctly deserializes objects from file"""
        self.storage.new(self.obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(self.obj_key, self.storage.all())
        self.assertEqual(self.storage.all()[self.obj_key].id, self.obj.id)

    def test_reload_no_file(self):
        """Test that reload() does nothing if the file doesn't exist"""
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_file_path_is_private(self):
        """Test that __file_path is a private attribute"""
        with self.assertRaises(AttributeError):
            getattr(self.storage, "__file_path")

    def test_objects_is_private(self):
        """Test that __objects is a private attribute"""
        with self.assertRaises(AttributeError):
            getattr(self.storage, "__objects")


if __name__ == "__main__":
    unittest.main()
