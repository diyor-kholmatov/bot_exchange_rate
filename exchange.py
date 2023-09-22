import requests

r = requests.get("https://nbu.uz/exchange-rates/json/").json()

json = list(filter(lambda x: x['code'] == "USD", r))
json1 = list(filter(lambda x: x['code'] == "CNY", r))
value = json[0]['cb_price']
value1 = json1[0]['cb_price']
print(f'Доллар США стоит {value} узбекских сум')
print(f'Китайский юань стоит {value1} узбекских сум')
print(f'Доллар США стоит {value1} Китайский юань')