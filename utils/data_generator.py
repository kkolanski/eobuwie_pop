from faker import Faker

class DataGenerator:
    """
    Generates Data for tests
    """
    def __init__(self):
        fake = Faker("pl_PL")
        self.customer_first_name = fake.first_name()
        self.customer_last_name = fake.last_name()