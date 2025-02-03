import pandas as pd
from src import logger

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.basket = None
        logger.info(f"File Path - {file_path}")

    def load_data(self):
        """Loads transaction data and converts it to a one-hot encoded DataFrame."""
        data = pd.read_csv(self.file_path)  # Assumes columns: [TransactionID, Item]
        
        # Pivot to one-hot encoding format
        basket = data.pivot_table(index='documentno', columns='name', aggfunc=lambda x: 1, fill_value=0)
        self.basket = basket.astype(bool)

    def get_basket(self):
        """Returns the processed transaction data."""
        if self.basket is None:
            self.load_data()
        return self.basket