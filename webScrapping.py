import requests
from bs4 import BeautifulSoup


data = requests.get("https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm")

soup = BeautifulSoup(data.content, 'html.parser')
movies_table = soup.find('table', {'class':'findList'})


rows = movies_table.findAll('tr')

for row in rows:
    rowdata = row.findAll('td')
    title = rowdata[1].a.text

    subUrl = rowdata[1].a['href']
    subData = requests.get("https://www.imdb.com"+subUrl)
    subSoup = BeautifulSoup(subData.content, 'html.parser')

    genre = subSoup.find('div', {'class': 'ipc-chip-list GenresAndPlot__OffsetChipList-sc-cum89p-5 dZdTje'})

    if subSoup.find('div', {'class': 'ipc-chip-list GenresAndPlot__OffsetChipList-sc-cum89p-5 dZdTje'}):
        print(title, genre.a.text)