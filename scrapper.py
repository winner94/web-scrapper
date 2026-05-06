import requests

def print_rates(rates):
    for r in rates:
        print(f"{r['code']:<5} |\t{r['currency']:<35} | {r['mid']:<5}")

def find_rates(rates, code):
    for r in rates:
        if r['code'] == code:
            return r
    return None

url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
response = requests.get(url)

data = response.json()
table = data[0]
rates = table["rates"]


currency = input("Enter currency code: ").upper()
result = find_rates(rates, currency)
print_rates([result]) if result else print("Not found")