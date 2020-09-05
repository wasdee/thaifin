def get_beta(stock_symbol):
    import requests
    from bs4 import BeautifulSoup

    stock_symbol = stock_symbol.upper()

    url = "https://www.set.or.th/set/factsheet.do"

    querystring = {
        "symbol": stock_symbol,
        "ssoPageId": "3",
        "language": "th",
        "country": "TH",
    }

    payload = ""
    headers = {
        "cookie": "JSESSIONID=B9EDD7F57C38D5300E5CE50AECD7989A.ITNPT-SET-TC01; route=4335e782ba8cf4516add92e65fa3c2d1",
        "authority": "www.set.or.th",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site": "none",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "accept-language": "en-US,en;q=0.9,th;q=0.8",
    }

    response = requests.request(
        "GET", url, data=payload, headers=headers, params=querystring
    )

    soup = BeautifulSoup(response.text, "html.parser")

    return [
        ele.text.strip()
        for ele in soup.table.find("td", text="Beta").parent.find_all("td")[1:]
    ]
