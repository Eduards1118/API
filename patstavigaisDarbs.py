import records
import requests
import json

# 4.1
response = requests.get(
    "https://pro2025.azurewebsites.net/books"
)
print(response)
print("Status code:", response.status_code)


if response.status_code == 200:
    print("Serveris strada")
else:
    print("Serveris neatbild")

# 4.2
data = response.json()
if data:
    print("Ir dati")
else:
    print("Nav datu")


for i in data:
    print(f'Gramata"{i["name"]}", {i["year_published"]}. gads, {i["pages"]} lpp')

# 4.3
book_names = []

for i in data:
    book_names.append(i["name"])

with open("nosaukumi.json", "w", encoding="utf-8") as file:
    json.dump(book_names, file)


# 4.4
oldest_book = data[0]

for i in data:
    if i["year_published"] < oldest_book["year_published"]:
        oldest_book = i
print("\nVisvecaka gramata:", oldest_book["name"])


# 4.5
all_pages = 0
all_price = 0

for i in data:
    all_pages += int(i["pages"])
    all_price += float(i["price"])

average_price = all_price / len(data)

print("Kopejais lapu skaits:", all_pages)
print("Videja cena:", round(average_price, 2))


# 4.6
def garakais_nosaukums(book_list):
    longest = book_list[0]

    for i in book_list:
        if len(i["name"]) > len(longest["name"]):
            longest = i
    return longest

book = garakais_nosaukums(data)

print("\nGramatas nosaukums:", book["name"])
print("Autors:", book["author"])
print("Gads:", book["year_published"])

# 4.7
all_books = []

for i in data:
    if not i["author"]:
        i["author"] = "Nav noradits"

    all_books.append(i)

# 4.8
authors = []

for i in all_books:
    if i["author"] not in authors:
        authors.append(i["author"])

authors.sort()

print("\nAutori:")
for i in authors:
    print(i)

# 4.9
author_count = {}

for i in all_books:
    author = i["author"]

    if author in author_count:
        author_count[author] += 1
    else:
        author_count[author] = 1

best_author = max(author_count, key=author_count.get)

print(f'Autors, kuram ir visvairak gramatu ({author_count[best_author]}), - {best_author}:')

count = 1
for i in all_books:
    if i["author"] == best_author:
        print(f'{count}. "{i["name"]}"')
        count += 1

# 4.10
journals_response = requests.get(
    "https://pro2025.azurewebsites.net/journals"
)

journals_data = journals_response.json()

journal_list = []

for i in journals_data[:10]:
    journal_list.append({
        "name": i["name"],
        "publisher": i["publisher"]
    })

print(journal_list)


def add_journal(journal_list):
    name = input("Nosaukums: ")
    publisher = input("Izdevejs: ")

    journal_list.insert(0, {
        "name": name,
        "publisher": publisher
    })


def delete_last_journal(journal_list):
    journal_list.pop()


add_journal(journal_list)
delete_last_journal(journal_list)

print(journal_list)

