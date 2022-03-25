"""Classes for melon orders."""

import random

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""


    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax    

    @staticmethod
    def get_base_price():
        """Calculate base price"""

        return random.randint(5, 9)

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    
     
class GovernmentMelonOrder(AbstractMelonOrder):
    """Melon order with the US Government"""  

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "government", 0.0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        # if passed = True:
        self.passed_inspection = passed

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "domestic", 0.08)

   


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        # def __init__(self, species, qty, order_type, tax):
        super().__init__(species, qty, "international", 0.17)

        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
