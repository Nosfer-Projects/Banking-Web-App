from unittest import TestCase
import sys
path = r'path to main folder "Banking-web-app"'
sys.path.append(path)

from modules.customer import Customer



class TestCustomer(TestCase):
    def setUp(self):
        self.customer_data = ["1", "123", "pass", "Nick", "Jones", 400 ]
        self.customer = Customer(self.customer_data)
    def test_customer_creation(self):
        self.assertEqual(self.customer.number, "1")
        self.assertEqual(self.customer.customer_id, "123")
        self.assertEqual(self.customer.password, "pass")
        self.assertEqual(self.customer.name, "Nick")
        self.assertEqual(self.customer.surname, "Jones")
        self.assertEqual(self.customer.balance, 400)




 


