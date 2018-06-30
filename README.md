BTC Markets python client
=================

A client implementation of [BTC Markets trading and account management API] (https://github.com/BTCMarkets/API) in python.

Expects keys.json containing two json key/value pairs:
```
{ "key" : "your-public-api-key", "secret" : "your-private-api-key" }
```

Example Usage:
```
client = BTCMarkets ('api key', 'private key') 
print client.account_balance()
```

TO DO List:
* error handling for http request, input parameter and json encoding of response
* support for http get query string
