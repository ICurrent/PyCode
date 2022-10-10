from urllib import response
import requests
import json

url = "https://api.exchangeratesapi.io/"
response = requests.get(url)

date = input("Enter the date in 'yyyy-mm-dd' OR type latest: ")
base_currency = input("Enter inital currency e.g NGN, USD: ")
to_currency = input("Enter final currency : ")
amount = input(f"How much {base_currency} do you want to convert?: ")

if date and base_currency and to_currency and amount:
    new_url = url + date + "?symbols=" + base_currency + "," + to_currency

if date == "latest":
    new_url = url + "latest?symbols=" + base_currency + "," + to_currency
else:
    print("You have provided invalid information.")
    exit()
response = requests.get(new_url)

if response.ok is False:
        print(f"{response.json()['error']}")
else:
    data = response.json()

    convert = (float(amount)/float(data['rates'][base_currency])) * float(data['rates'][to_currency])
    convert = round(convert, 2)
    print(f"The amount equivalent to {base_currency} {amount} is {to_currency} {convert}")

