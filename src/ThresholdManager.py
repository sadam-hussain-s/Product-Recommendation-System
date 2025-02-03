from src import logger

class ThresholdManager:
    def __init__(self, min_support=0.01, max_support=0.1, default_confidence=0.5):
        self.min_support = min_support
        self.max_support = max_support
        self.default_confidence = default_confidence

    def calculate_dynamic_support(self, num_transactions: int):
        """Dynamically sets the support threshold based on the dataset size."""
        return max(self.min_support, min(self.max_support, 50 / num_transactions))

    def get_dynamic_thresholds(self, num_transactions: int):
        """Returns dynamic min_support and min_confidence values."""
        dynamic_support = self.calculate_dynamic_support(num_transactions)
        return dynamic_support, self.default_confidence