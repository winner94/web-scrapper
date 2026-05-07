import requests
import csv

def print_rates(rates):
    for r in rates:
        print(f"{r['code']:<5} |\t{r['currency']:<35} | {r['mid']:<5}")

def find_rates(rates, code):
    for r in rates:
        if r['code'] == code:
            return r
    return None

def save_to_csv(rates):
    with open("rates.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ['code', 'currency', 'mid']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rates)


url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
response = requests.get(url)

data = response.json()
table = data[0]
rates = table["rates"]


#currency = input("Enter currency code: ").upper()
#result = find_rates(rates, currency)
#print_rates([result]) if result else print("Not found")
save_to_csv(rates)