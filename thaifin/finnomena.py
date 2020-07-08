import requests
import json

def get_financial_sheet(securityID, fiscal=2009):

    url = "https://www.finnomena.com/fn3/api/stock/financial"

    querystring = {"securityID": str(securityID),"fiscal":str(fiscal)}

    payload = ""
    headers = {
        'connection': "keep-alive",
        'accept': "application/json, text/plain, */*",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.finnomena.com/stock/SCB?bt_id=60",
        'accept-language': "en-US,en;q=0.9,th;q=0.8"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    return json.loads(response.text)['data']

def get_stock_list():

    url = "https://www.finnomena.com/fn3/api/stock/list"

    payload = ""
    headers = {
        'connection': "keep-alive",
        'accept': "application/json, text/plain, */*",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.finnomena.com/stock/SCB?bt_id=60",
        'accept-language': "en-US,en;q=0.9,th;q=0.8",
        # 'cookie': "finnakies=5MLMJIS20200601; _ga=GA1.2.1303959403.1591006631; _fbp=fb.1.1591006631416.2138659500; PHPSESSID=on32ipkohq41hfv1dcu2eutuou; anspress_session=83fa3179f4e427a9e00e328d0d2ba568; _gid=GA1.2.1759981110.1594035335; terms_cond_accepted=false; _cbclose=1; _cbclose47370=1; _uid47370=595254B6.3; _ctout47370=1; verify=test; finnakies-ss=635VtLn20200706; _hjid=053a69da-8d52-4064-b1ce-82118f02ac68; _hjAbsoluteSessionInProgress=1; __cfduid=dad57d546f7805625889ebd80a183dc091594035361; _hjDonePolls=376740; visit_time=10"
        }

    response = requests.request("GET", url, data=payload, headers=headers)

    return json.loads(response.text)['data']