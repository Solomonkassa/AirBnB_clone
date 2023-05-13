#!/usr/bin/python3
"""Unittests for file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
#import json
import models
import unittest
#from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
  """Unittests for testing instantiation of the FileStorage class."""

  def test_FileStorage_instantiation_no_args(self):
    self.assertEqual(type(FileStorage()), FileStorage)

  def test_FileStorage_instantiation_with_arg(self):
    with self.assertRaises(TypeError):
      FileStorage(None)

  def test_FileStorage_file_path_is_private_str(self):
    self.assertEqual(str, type(FileStorage._FileStorage__file_path))

  def testFileStorage_objects_is_private_dict(self):
    self.assertEqual(dict, type(FileStorage._FileStorage__objects))

  def test_storage_initializes(self):
    self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
  """Unittests for testing methods of the FileStorage class."""

  @classmethod
  def setUp(self):
    try:
      os.rename("file.json", "tmp")
    except IOError:
      pass

  @classmethod
  def tearDown(self):
    try:
      os.remove("file.json")
    except IOError:
      pass
    try:
      os.rename("tmp", "file.json")
    except IOError:
      pass
    FileStorage._FileStorage__objects = {}

  def test_all(self):
    self.assertEqual(dict, type(models.storage.all()))

  def test_all_with_arg(self):
    with self.assertRaises(TypeError):
      models.storage.all(None)

  def test_new(self):
    bm = BaseModel()
    usr = User()
    sta = State()
    pla = Place()
    ct = City()
    amy = Amenity()
    rev = Review()
    models.storage.new(bm)
    models.storage.new(usr)
    models.storage.new(sta)
    models.storage.new(pla)
    models.storage.new(ct)
    models.storage.new(amy)
    models.storage.new(rev)
    self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
    self.assertIn(bm, models.storage.all().values())
    self.assertIn("User." + usr.id, models.storage.all().keys())
    self.assertIn(usr, models.storage.all().values())
    self.assertIn("State." + sta.id, models.storage.all().keys())
    self.assertIn(sta, models.storage.all().values())
    self.assertIn("Place." + pla.id, models.storage.all().keys())
    self.assertIn(pla, models.storage.all().values())
    self.assertIn("City." + ct.id, models.storage.all().keys())
    self.assertIn(ct, models.storage.all().values())
    self.assertIn("Amenity." + amy.id, models.storage.all().keys())
    self.assertIn(amy, models.storage.all().values())
    self.assertIn("Review." + rev.id, models.storage.all().keys())
    self.assertIn(rev, models.storage.all().values())

  def test_new_with_args(self):
    with self.assertRaises(TypeError):
      models.storage.new(BaseModel(), 1)

  def test_save(self):
    bm = BaseModel()
    usr = User()
    sta = State()
    pla = Place()
    ct = City()
    amy = Amenity()
    rev = Review()
    models.storage.new(bm)
    models.storage.new(usr)
    models.storage.new(sta)
    models.storage.new(pla)
    models.storage.new(ct)
    models.storage.new(amy)
    models.storage.new(rev)
    models.storage.save()
    save_text = ""
    with open("file.json", "r") as f:
      save_text = f.read()
      self.assertIn("BaseModel." + bm.id, save_text)
      self.assertIn("User." + usr.id, save_text)
      self.assertIn("State." + sta.id, save_text)
      self.assertIn("Place." + pla.id, save_text)
      self.assertIn("City." + ct.id, save_text)
      self.assertIn("Amenity." + amy.id, save_text)
      self.assertIn("Review." + rev.id, save_text)

  def test_save_with_arg(self):
    with self.assertRaises(TypeError):
      models.storage.save(None)

  def test_reload(self):
    bm = BaseModel()
    usr = User()
    sta = State()
    pla = Place()
    ct = City()
    amy = Amenity()
    rev = Review()
    models.storage.new(bm)
    models.storage.new(usr)
    models.storage.new(sta)
    models.storage.new(pla)
    models.storage.new(ct)
    models.storage.new(amy)
    models.storage.new(rev)
    models.storage.save()
    models.storage.reload()
    objs = FileStorage._FileStorage__objects
    self.assertIn("BaseModel." + bm.id, objs)
    self.assertIn("User." + usr.id, objs)
    self.assertIn("State." + sta.id, objs)
    self.assertIn("Place." + pla.id, objs)
    self.assertIn("City." + ct.id, objs)
    self.assertIn("Amenity." + amy.id, objs)
    self.assertIn("Review." + rev.id, objs)

  def test_reload_with_arg(self):
    with self.assertRaises(TypeError):
      models.storage.reload(None)


if __name__ == "__main__":
  unittest.main()
