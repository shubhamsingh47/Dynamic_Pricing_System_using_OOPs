from .pricing_strategy import DemandBasedPricing, CompetitorPricing, InventoryPricing, UserBehaviourPricing


class PricingFactory:
    @staticmethod      # It will not interact with class attributes
    def get_pricing_strategy(strategy_type, **kwargs):
        strategies = {
            "demand": DemandBasedPricing(kwargs.get("demand_factor", 0.1)),
            "competitor": CompetitorPricing(kwargs.get("competitor_price", 100)),
            "inventory": InventoryPricing(
                kwargs.get("inventory_level", 50),
                kwargs.get("threshold", 20)
            ),
            "UserBehaviour": UserBehaviourPricing(kwargs.get("user_data", {}))
        }
        if strategy_type not in strategies:
            print(f"Invalid strategy_type: '{strategy_type}'. Choose from {list(strategies.keys())}.")

        return strategies[strategy_type]
