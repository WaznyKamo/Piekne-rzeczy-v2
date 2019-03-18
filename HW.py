# Prezentacja walut z strony NBP

import requests
from bs4 import BeautifulSoup


url = "https://www.nbp.pl/home.aspx?f=/kursy/kursya.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")
table_html = soup.find('table', attrs={"class": "pad5"})

for currency_html in table_html.findAll('tr'):
    currency_name = currency_html.find("td", attrs={"class": "bgt1 left"})
    currency_value = currency_html.findAll("td", attrs={"class": "bgt1 right"})
    if currency_name is not None:
        currency_name = currency_name.text
        currency_value = currency_value[1].text
        print(currency_name, ":\t\t", currency_value)

