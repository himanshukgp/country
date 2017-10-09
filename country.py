import requests
from bs4 import BeautifulSoup

url = "http://www.worldclasslearning.com/general-knowledge/list-countries-capital-currencies-languages.html"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
#print (soup.prettify())

tables = soup.findAll("table")

for table in tables:
	list_of_rows = []
	for row in table.findAll('tr'):
		list_of_cells = []
		for cell in row.findAll('td'):
			text = cell.text.replace('&nbsp;', '')
			list_of_cells.append(text)
		list_of_rows.append(list_of_cells)

print (list_of_rows)



