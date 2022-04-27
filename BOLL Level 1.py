#Top Skill 1. Python Coding
#Import Python Libraries
import requests
from IPython.display import Image, display

#Top Skill 2. Get API Data
getApiData = requests.get('https://coinballer.io/api/technical-indicators-daily/APIKEY')
ApiData = getApiData.json()

#Top Skill 3. Variables
ApiDataToday = ApiData[-1]
BollingerMiddle = ApiDataToday['bollinger_middle']
BTCPrice = ApiDataToday['price_close']

#Top Skill 4. If Statements
if BTCPrice > BollingerMiddle:
    Scoreboard = 'https://i.imgur.com/wjbQ2dq.png'
else: Scoreboard = 'https://i.imgur.com/C88GgnO.png'

print('BTC Price')
print(BTCPrice)
display(Image(Scoreboard))
print('BOLL')
