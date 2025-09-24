class Stock():
    def __init__(self, ticker: str, issuer: str, price: float):
        self.ticker = ticker
        self.issuer = issuer
        self.price = price

    def __str__(self):
        return f"<Stock: ticker={self.ticker}; issuer={self.issuer}; price={self.price}"