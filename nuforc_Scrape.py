from bs4 import BeautifulSoup
import requests
import pandas as pd

links = []
df_list = []
response = requests.get('https://nuforc.org/webreports/ndxevent.html')
soup = BeautifulSoup(response.content, "lxml")
table = soup.find('table')

for row in table.find_all('a', href=True):
    links.append(row['href'])

for link in links :
    url = f'https://nuforc.org/webreports/{link}'
    df = pd.read_html(url)
    data = df[0]
    df = pd.DataFrame(data)
    df_list.append(df)
df1 = pd.concat(df_list)

df1.to_csv(r'C:\Users\ckjar\Documents\_Projects\Ufo Analysis\ufo_data.csv', index=False, sep=';')
print('done')