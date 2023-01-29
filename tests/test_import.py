from unittest import TestCase
from modules.import_sql import Sql_import

class TestCustomer(TestCase):
    def setUp(self):
        customer = Sql_import()
        self.result = customer.data("admin")

    def test_data(self):
        self.assertTrue(self.result)

    
    def test_correct_data(self):
        mock_obj = MagicMock()
        mock_obj.show.return_value = self.result[-1] 
        customer = [1, "admin", "123", "John", "Smith", mock_obj.show()]
        self.assertEqual(self.result, customer)



