class CartePizzeria:
    def __init__(self):
        self.__pizzas = []

    @property
    def pizzas(self):
        return self.__pizzas

    def is_empty(self):
        return self.nb_pizzas() == 0

    def nb_pizzas(self):
        return len(self.pizzas)

    def add(self, element):
        if self.__contains_name(element.name):
            print(f"Element {element.name} is already registered with another name")
        elif self.__contains_pizza_ingredients(element.ingredients):
            print(f"Element {element.name} has the same ingredients as another pizza")
        else:
            self.pizzas.append(element)

    def __contains_name(self, name):
        for pizza in self.pizzas:
            if pizza.name == name:
                return True
        return False

    def __contains_pizza_ingredients(self, pizza_ingredients):
        for pizza in self.pizzas:
            if self.same_ingredients(pizza_ingredients, pizza.ingredients):
                return True
        return False

    def same_ingredients(self, ingredients_0, ingredients_1):
        return set(ingredients_0) == set(ingredients_1)

    def remove(self, name):
        found = False
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                found = True
                break
        if not found:
            print(f"Element {name} not found")


# Si vous avez également besoin de la classe Pizza pour tester la fonctionnalité, assurez-vous de l'importer et de la définir correctement.
class Pizza:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients


# Exemple d'utilisation
if __name__ == "__main__":
    carte = CartePizzeria()
    pizza1 = Pizza("Margherita", ["tomato", "mozzarella"])
    pizza2 = Pizza("Pepperoni", ["tomato", "mozzarella", "pepperoni"])

    carte.add(pizza1)
    carte.add(pizza2)

    print(carte.nb_pizzas())  # Output: 2

    carte.remove("Margherita")
    print(carte.nb_pizzas())  # Output: 1
