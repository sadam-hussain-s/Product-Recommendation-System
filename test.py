from src.DataLoader import DataLoader

data_loader = DataLoader('chn_processed_food_dec2024.csv')
basket = data_loader.get_basket()
print(basket)