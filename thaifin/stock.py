import arrow
import pandas as pd
from fuzzywuzzy import process

from thaifin.sources.finnomena import get_financial_sheet
from thaifin.sources.finnomena import get_stock_list


class Stock:
    @classmethod
    def search(cls, company_name: str, limit: int = 5):
        list_ = get_stock_list().data
        search_against = {x.thName + x.enName: x for x in list_}
        search_result = process.extract(company_name, search_against, limit=limit)
        return [cls(s[0].name) for s in search_result]

    @staticmethod
    def list_symbol():
        list_ = get_stock_list().data
        return [s.name for s in list_]

    @staticmethod
    def find_symbol(symbol: str):
        list_ = get_stock_list().data
        return next(obj for obj in list_ if obj.name == symbol)

    def __init__(self, symbol: str):
        symbol = symbol.upper()
        self.info = self.find_symbol(symbol)
        self.fundamental = get_financial_sheet(self.info.security_id).data
        self.updated = arrow.utcnow()
        # self.

    @property
    def symbol(self):
        return self.info.name

    @property
    def company_name(self):
        return self.info.enName

    @property
    def thai_company_name(self):
        return self.info.thName

    @property
    def quarter_dataframe(self):
        df = pd.DataFrame([s.dict(exclude={"SecurityID"}) for s in self.fundamental])
        # Quarter 9 means yearly values
        df = df[df.Quarter != 9]
        df["Time"] = df.Fiscal.astype(str) + "Q" + df.Quarter.astype(str)
        df = df.set_index("Time")
        df.index = pd.to_datetime(df.index).to_period("Q")
        df = df.drop(columns=["Fiscal", "Quarter"])
        return df

    @property
    def yearly_dataframe(self):
        df = pd.DataFrame([s.dict(exclude={"SecurityID"}) for s in self.fundamental])
        # Quarter 9 means yearly values
        df = df[df.Quarter == 9]
        df = df.set_index("Fiscal")
        df.index = pd.to_datetime(df.index, format="%Y").to_period("Y")
        df = df.drop(columns=["Quarter"])
        return df

    def __repr__(self):
        return f'<Stock "{self.symbol}" - updated {self.updated.humanize()}>'
