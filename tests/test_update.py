from unittest import TestCase
from update_sql import Sql_update
from import_sql import Sql_import

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