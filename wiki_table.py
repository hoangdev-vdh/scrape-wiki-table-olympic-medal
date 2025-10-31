import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/2020_Summer_Olympics_medal_table'

useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

headers = {
    'User-Agent': useragent
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable sortable sticky-header-multi plainrowheaders jquery-tablesorter'})
    
    data = []
    for row in table.find_all('tr'):
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    with open('olympic_medal_table.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    print("Finished")
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')