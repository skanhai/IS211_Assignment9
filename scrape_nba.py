#https://en.wikipedia.org/wiki/List_of_NBA_champions
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


url = "https://en.wikipedia.org/wiki/List_of_NBA_champions"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
tables = soup.find_all("table", class_="wikitable")


for index, table in enumerate(tables):
    rows = table.find_all("tr")

    table_data = []

    for row in rows:
        cells = row.find_all(["th", "td"])

        row_data = [cell.get_text(strip=True) for cell in cells]

        table_data.append(row_data)

    print(f"Table {index + 1}")
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))
    print("\n")
