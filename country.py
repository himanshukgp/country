import requests
from bs4 import BeautifulSoup

url = "http://www.worldclasslearning.com/general-knowledge/list-countries-capital-currencies-languages.html"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
#print (soup.prettify())

tables = soup.findAll("table")

for table in tables:
     if table.findParent("table") is None:
         print (str(table))
