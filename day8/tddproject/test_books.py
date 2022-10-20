import unittest
import os
import json
from app import create_app, db

class BookTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.from_pyfile('configtest.py')
        self.app.client = self.app.test_client
        self.book = {'name':'programming in python'}

        with self.app.app_context():
            db.create_all()

    def test_booklist_creation(self):
        res = self.app.client().post('/booklists',data = self.book)
        self.assertEqual(res.status_code,201)
        self.assertIn('programming in python',str(res.data))

    def test_booklist_getbooks(self):
        res = self.app.client().post('/booklists',data = self.book)
        self.assertEqual(res.status_code,201)
        res = self.app.client().get('/booklists')
        self.assertEqual(res.status_code,200)
        self.assertIn('programming in python',str(res.data))

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == '__main__':
    unittest.main()
        
