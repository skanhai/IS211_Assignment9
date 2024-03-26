#https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economic_Sciences
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import textwrap


url = "https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economic_Sciences"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
tables = soup.find_all("table", class_="wikitable")


for index, table in enumerate(tables):
    table_data = []

    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all(["th", "td"])

        row_data = []
        for cell in cells:
            text = cell.get_text(strip=True)
            wrapped_text = textwrap.fill(text, width=50)
            row_data.append(wrapped_text)

        table_data.append(row_data)

    print(f"Table {index + 1}")
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))
    print("\n")

