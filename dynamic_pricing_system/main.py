from database.db_config import Database
from pricing.product import Product
from pricing.factory import PricingFactory

# Database initialization
db = Database(password='Enter_your_password')

# Inserting sample products
db.insert_product("Laptop", 50000, "Electronics")
db.insert_product("Running Shoes", 1120, "Footwear")

# Fetch and apply pricing strategies
products = db.fetch_products()

for product in products:
    name, base_price, category = product[1], product[2], product[3]
    p = Product(name, base_price, category)

    strategy = PricingFactory.get_pricing_strategy("demand", demand_factor=0.2)
    print(f"{p.name} final price: ${strategy.calculate_price(p):.2f}")
