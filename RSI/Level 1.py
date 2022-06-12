#Top Skill 1. Python Coding
#Import Python Libraries
import requests
from IPython.display import Image, display

#Top Skill 2. Get API Data
getApiData = requests.get('https://coinballer.io/api/technical-indicators-daily/APIKEY')
ApiData = getApiData.json()

#Top Skill 3. Variables
ApiDataToday = ApiData[-1]
RSI = ApiDataToday['rsi']
BTC = ApiDataToday['price_close']

#Top Skill 4. If Statements
if RSI > 50:
    Scoreboard = 'https://i.imgur.com/aCTsoA0.png'
else: Scoreboard = 'https://i.imgur.com/8Li7d4A.png'

print('Bitcoin Price')
print(BTC)
print('RSI')
print(RSI)
display(Image(Scoreboard))
