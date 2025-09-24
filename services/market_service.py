import db
from domain.Stock import Stock
from typing import List

def get_stocks() -> List[Stock]:
    return db.query_all_stocks()