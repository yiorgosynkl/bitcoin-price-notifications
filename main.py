import requests 
import json
import time
import webbrowser
import pprint

from details import private_api_key, ifttt_event_name, ifttt_key

def getBitcoinPrice(): # Function to get the info
    coinmarketcap_quotes_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest' # Coinmarketcap API url

    parameters = { 'slug': 'bitcoin', 'convert': 'USD' } # API parameters to pass in for retrieving specific cryptocurrency data

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY':  private_api_key
    } # Replace 'YOUR_API_KEY' with the API key you have recieved in the previous step

    session = requests.Session()
    session.headers.update(headers)

    response = session.get(coinmarketcap_quotes_url, params=parameters)

    info = json.loads(response.text)
    # pprint.pprint(info)
    price = info['data']['1']['quote']['USD']['price']
    pprint.pprint(price)
    return price

# trigger IFTTT webhook
def sendNotification(price):
    ifttt_webhook_url = f"https://maker.ifttt.com/trigger/{ifttt_event_name}/with/key/{ifttt_key}" 
    data = {
        'value1': price 
    }
    requests.post(ifttt_webhook_url, json=data)

def run():
    price = getBitcoinPrice() # Calling the function to get the statistics
    sendNotification(price)

run()

