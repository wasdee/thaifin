import pandas as pd
from furl import furl


def get_dividend(symbol: str):
    symbol = symbol.upper()
    f_url = furl(
        "https://www.settrade.com/C04_07_stock_rightsandbenefit_p1.jsp?txtSymbol=SCB&ssoPageId=15&selectPage=7"
    )
    f_url.args["txtSymbol"] = symbol
    dfs = pd.read_html(f_url.url)
    df = dfs[0]
    return df
