import requests
import json
url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
currency_from = "NPR"
currency_to = "USD"
amount = "50"
querystring = {"from":currency_from,"to":currency_to,"amount": amount}

headers = {
	"X-RapidAPI-Key": "970b8bb5e5mshb75460a8d5c5c60p17afb3jsnd738436ab2d3",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = json.loads(response.text)

converted_amount = data['result']['convertedAmount']
formatted = "{:,.2f}".format(converted_amount)
print(formatted)