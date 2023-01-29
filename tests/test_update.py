from unittest import TestCase
from modules.update_sql import Sql_update
from modules.import_sql import Sql_import

class TestUpdate(TestCase):
        def setUp(self):
            data = Sql_import()
            self.result = data.data("admin")
            self.mock_obj = MagicMock()
            self.mock_obj.show.return_value = self.result[-1] 
            customer = Sql_update()
            self.update = customer.update("admin", self.mock_obj.show())

        def test_data(self):
            self.assertTrue(self.result)

        def test_correct_data(self):
            customer = [1, "admin", "123", "John", "Smith", self.mock_obj.show()]
            self.assertEqual(self.result, customer)
