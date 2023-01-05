from unittest import TestCase
from import_sql import Sql_import

class TestCustomer(TestCase):
    def setUp(self):
        customer = Sql_import()
        self.result = customer.data("admin")

    def test_data(self):
        self.assertTrue(self.result)

    
    def test_correct_data(self):
        customer = [1, "admin", "123", "John", "Smith", 4]
        self.assertEqual(self.result, customer)



