import unittest   # For Unit Testing
from dynamic_pricing_system.pricing.pricing_strategy import CompetitorPricing, InventoryPricing, \
    DemandBasedPricing, UserBehaviourPricing
from dynamic_pricing_system.pricing.product import Product


class TestPricingStrategies(unittest.TestCase):
    def setUp(self) -> None:
        self.product = Product("Laptop", 50000, "Electronics")

    def test_demand_based_pricing(self):
        strategy = DemandBasedPricing(0.2)
        expected_price = 50000 * 1.2     # Check the initial formula in pricing_strategy file to get expected price
        self.assertAlmostEqual(strategy.calculate_price(self.product), expected_price)

    def test_competitor_based_pricing(self):
        strategy = CompetitorPricing(48000)
        expected_price = (50000 + 48000) / 2  # Average of base price and competitor price
        self.assertAlmostEqual(strategy.calculate_price(self.product), expected_price)

    def test_inventory_based_pricing_low_stock(self):
        strategy = InventoryPricing(inventory_level=8, threshold=12)  # Low stock
        expected_price = 50000 * 1.2  # 20% increase for low stock
        self.assertAlmostEqual(strategy.calculate_price(self.product), expected_price)

    def test_inventory_based_pricing_high_stock(self):
        strategy = InventoryPricing(inventory_level=50, threshold=12)  # High stock
        expected_price = 50000 * 0.9  # 10% discount for high stock
        self.assertAlmostEqual(strategy.calculate_price(self.product), expected_price)

    def user_based_pricing(self):
        strategy = UserBehaviourPricing(
            {"loyal_customer": True, "frequent_visitor": True})  # Loyal and frequent customer
        expected_price = 50000 * 1.1
        expected_price -= expected_price * 0.2
        self.assertAlmostEqual(strategy.calculate_price(self.product), expected_price)


if __name__ == "__main__":
    unittest.main()
