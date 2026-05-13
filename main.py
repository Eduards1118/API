from itertools import count

import records
import requests

response = requests.get(
    "https://data.gov.lv/dati/lv/api/action/datastore_search?resource_id=ca236c1e-7dc0-46f5-ba98-a46e3d29f870&limit=20"
)

print(response)
print("Status code:", response.status_code)

data = response.json()

if response.status_code == 200:
    print("Serveris strada")
else:
    print("Serveris neatbild")


print("\nPašvaldības un kopējais izglītojamo skaits")
for i in data['result']['records']:
    print(i["Pasvaldiba"], "-", i["Kopejais_izglitojamo_skaits"])


print("\nVidusskolēnu skaits pa pašvaldībām")
for i in data['result']['records']:
    vidusskola = (
        i["10_klase"] +
        i["11_klase"] +
        i["12_klase"]
    )
    print(i["Pasvaldiba"], "-", vidusskola)


min_count = int(records[0]['Kopejais_izglitojamo_skaits'])
min_city = records[0]['Pasvaldiba']

for item in records:
    municipality = item['Pasvaldiba']
    count = int(item['Kopejais_izglitojamo_skaits'])

    if count < min_count:
        min_count = count
        min_city = municipality

print('\nPasvaldiba ar vismazako izglitojamo skaitu: ')
print(min_city, '-', min_count)

