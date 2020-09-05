def test_fin():
    pass


def test_stock():
    import thaifin

    stock = thaifin.Stock("PTT")
    stock_list = thaifin.Stock.list_symbol()
    print(thaifin.Stock.list_symbol())
    print(thaifin.Stock.search("จัสมิน"))
    dfq = stock.quarter_dataframe
    dfy = stock.yearly_dataframe
    print(stock)
