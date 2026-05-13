import records
import requests

response = requests.get(
    "https://pro2025.azurewebsites.net/books"
)

print(response)
print("Status code:", response.status_code)



if response.status_code == 200:
    print("Serveris strada")
else:
    print("Serveris neatbild")


data = response.json()
if data:
    print("Ir dati")
else:
    print("Nav datu")


for i in data:
    print(f'Gramata"{i["name"]}", {i["year_published"]}. gads, {i["pages"]} lpp')