import csv

dati = []
with open("agenti.csv", "r", encoding="utf-8") as datne:
    lasitajs = csv.DictReader(datne, delimiter=";")

    for rinda in lasitajs:
        dati.append(rinda)

# 1. uzdevums
print("Visi dati:")
for ieraksts in dati:
    print(ieraksts)

# 2. uzdevums
derigie_tipi = ["Izglītības iestāde", "Valsts iestāde"]

filtreti_dati = []

for ieraksts in dati:
    if ieraksts["TIPS"] in derigie_tipi:
        filtreti_dati.append(ieraksts)

print("\nFiltrētie dati:")
for ieraksts in filtreti_dati:
    print(ieraksts)

# 3. uzdevums
rigas_dati = []

for ieraksts in filtreti_dati:
    if "Rīga" in ieraksts["ADRESE"]:
        rigas_dati.append({
            "NOSAUKUMS": ieraksts["NOSAUKUMS"],
            "ADRESE": ieraksts["ADRESE"]
        })

print("\n3. uzdevums — iestādes Rīgā:")
for ieraksts in rigas_dati:
    print(ieraksts)

# 4. uzdevums
sakartoti_dati = sorted(rigas_dati, key=lambda x: x["NOSAUKUMS"])

print("\n4. uzdevums — sakārtoti dati:")
for ieraksts in sakartoti_dati:
    print(ieraksts)

