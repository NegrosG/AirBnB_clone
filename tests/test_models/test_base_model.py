#!/usr/bin/python3
"""
Module for Base_models Unittest
"""
import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    unittest for BaseModel
    """

    def setUp(self):
        """
        Setup for temporary file path
        """
        try:
            os.rename("file.json", "tmp.json")

        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Teardown for temporary file path
        """
    try:
        os.remove("file.json")

    except FileNotFoundError:
        pass
    try:
        os.rename("tmp.json", "file.json")

    except FileNotFoundError:
        pass

    def test_init(self):
        """
        Test for init method
        """
        model_test = BaseModel()
        self.assertIsNotNone(model_test.id)
        self.assertIsNotNone(model_test.created_at)
        self.assertIsNotNone(model_test.updated_at)

    def test_save(self):
        """
        Test for the save method
        """
        model_test = BaseModel()
        initial_updated = model_test.updated_at
        current_updated = model_test.save()

        self.assertNotEqual(initial_updated, current_updated)

    def test_to_dict(self):
        """
        Test for the to_dict method
        """
        model_test = BaseModel()

        model_test_dict = model_test.to_dict()

        self.assertIsInstance(model_test_dict, dict)

        self.assertEqual(model_test_dict["__class__"], 'BaseModel')
        self.assertEqual(model_test_dict['id'], model_test.id)
        self.assertEqual(model_test_dict['created_at'], 
                         model_test.created_at.isoformat())
        self.assertEqual(model_test_dict["updated_at"], 
                         model_test.created_at.isoformat())

    def test_str(self):
        """
        Test for the string representation
        """
        model_test = BaseModel()

        self.assertTrue(str(model_test).startswith('[BaseModel]'))
        self.assertIn(model_test.id, str(model_test))
        self.assertIn(str(model_test.__dict__), str(model_test))


if __name__ == "__main__":
    unittest.main()
