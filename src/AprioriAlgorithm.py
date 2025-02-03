from mlxtend.frequent_patterns import apriori, association_rules,fpgrowth
import pandas as pd
from src import logger

class AprioriAlgorithm:
    def __init__(self, basket: pd.DataFrame, support: float, confidence: float):
        self.basket = basket
        self.min_support = support
        self.min_confidence = confidence
        self.rules = None
        logger.info(f"Support - {support}, Confidence - {confidence}")

    def run(self):
        logger.info("Start to generate the rules")
        frequent_itemsets = fpgrowth(self.basket, min_support=self.min_support, use_colnames=True)
        self.rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=self.min_confidence)
        logger.info("Completed to generate the rules")

    def get_rules(self):
        """Returns the generated association rules."""
        if self.rules is None:
            self.run()
        return self.rules.sort_values(by="lift", ascending=False).to_dict(orient="records")