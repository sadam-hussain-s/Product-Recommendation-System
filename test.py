from src.DataLoader import DataLoader
from src.ThresholdManager import ThresholdManager
from src.AprioriAlgorithm import AprioriAlgorithm
import pandas as pd

data_loader = DataLoader('chn_processed_food_dec2024.csv')
basket = data_loader.get_basket()
threshold_manager = ThresholdManager()

def get_rules(min_support: float = None, min_confidence: float = None):
    """Fetch association rules with dynamic or user-defined thresholds."""
    num_transactions = len(basket)

    # Use dynamic thresholds if none are provided
    if min_support is None or min_confidence is None:
        min_support, min_confidence = threshold_manager.get_dynamic_thresholds(num_transactions)

    apriori_alg = AprioriAlgorithm(basket, min_support, min_confidence)
    rules = apriori_alg.get_rules()
    return {"min_support": min_support, "min_confidence": min_confidence, "rules": rules}

res = get_rules(0.01,0.50)
val=res['rules']

def inspect(res,count):
  lhs = [tuple(res[result]['antecedents']) for result in range(count)]
  rhs = [tuple(res[result]['consequents']) for result in range(count)]
  support =  [res[result]['support'] for result in range(count)]
  confidence = [ res[result]['confidence'] for result in range(count)]
  lift = [ res[result]['lift'] for result in range(count)]
  return list(zip(lhs,rhs,support,confidence,lift))

resultsinDataFrame = pd.DataFrame(inspect(val,len(val)), columns = ['Antecedents', 'Consequents', 'Support', 'Confidence', 'Lift'])
print(resultsinDataFrame.head())