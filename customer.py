class Customer():
    """
    A class for creating a specific client after downloading data from the server
    """
    def __init__(self, list):
        self.number = list[0]
        self.customer_id = list[1]
        self.password = list[2]
        self.name= list[3]
        self.surname= list[4]
        self.balance= list[5]
