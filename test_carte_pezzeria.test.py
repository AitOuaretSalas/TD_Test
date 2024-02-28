import unittest
from cartePizzeria import CartePizzeria, Pizza

class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        self.carte = CartePizzeria()

    def test_add_unique_name(self):
        pizza1 = Pizza("Margherita", ["tomato", "mozzarella"])
        self.carte.add(pizza1)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    # Autres méthodes de test...

if __name__ == '__main__':
    unittest.main()
