from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, product):
        pass


class DemandBasedPricing(PricingStrategy):
    def __init__(self, demand_factor):
        self.demand_factor = demand_factor

    def calculate_price(self, product):
        return product.base_price * (1 + self.demand_factor)


class CompetitorPricing(PricingStrategy):
    def __init__(self, competitor_price):
        self.competitor_price = competitor_price

    def calculate_price(self, product):
        return (product.base_price + self.competitor_price) / 2  # Averaging Strategy


class InventoryPricing(PricingStrategy):
    HIGH_DEMAND_MULTIPLIER = 1.2
    LOW_DEMAND_MULTIPLIER = 0.9

    def __init__(self, inventory_level, threshold):
        self.inventory_level = inventory_level
        self.threshold = threshold

    def calculate_price(self, product):
        if self.inventory_level < self.threshold:
            return product.base_price * self.HIGH_DEMAND_MULTIPLIER  # Product is in high demand, therefore we increase price
        else:
            return product.base_price * self.LOW_DEMAND_MULTIPLIER  # Product is in low demand, therefore we decrease price


class UserBehaviourPricing(PricingStrategy):
    def __init__(self, user_data):
        self.user_data = user_data

    def calculate_price(self, product):
        loyalty_discount = 0.2 if self.user_data.get('loyal_customer') else 0  # 20% discount
        frequent_user = 1.1 if self.user_data.get('frequent_visitor') else 1  # 10% Premium

        price = product.base_price * frequent_user
        price -= price * loyalty_discount

        return round(price, 2)