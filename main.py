import json

from btcmarkets import BTCMarkets

with open('keys.json', 'r') as f:
    config = json.load(f)

api_key = config['key']
private_key = config['secret']

client = BTCMarkets (api_key, private_key) 

#print(client.trade_history('AUD', 'BTC', 10, 1))

#print(client.order_detail([1234, 213456]))
 
#print(client.order_create('AUD', 'LTC', 100000000, 100000000, 'Bid', 'Limit', '1'))

print(client.get_market_tick('ETH','AUD'))
