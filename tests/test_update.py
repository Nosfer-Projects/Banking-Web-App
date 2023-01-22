from unittest import TestCase
import sys
path = r'path to main folder "Banking-web-app"'
sys.path.append(path)
from modules.update_sql import Sql_update
from modules.import_sql import Sql_import

class TestUpdate(TestCase):
        def setUp(self):
            customer = Sql_update()
            self.update = customer.update("admin", 1000)
            data = Sql_import()
            self.result = data.data("admin")
        def test_data(self):
            self.assertTrue(self.result)

        def test_correct_data(self):
            customer = [1, "admin", "123", "John", "Smith", 1000]
            self.assertEqual(self.result, customer)