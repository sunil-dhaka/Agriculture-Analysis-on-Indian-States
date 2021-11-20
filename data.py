'''
to get data from API hosted on data.gov servers
'''

import requests
import login 
# personal creds file for api-key 
# simply set api_key var in login.py file to your api_key

api_key=login.api_key

url=f'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key={api_key}&format=csv&offset=0&limit=10000'

# as size is about 15mb takes a bit time depending on net speed
r=requests.get(url)

with open('daily_price.csv','w') as file:
    file.write(r.text)