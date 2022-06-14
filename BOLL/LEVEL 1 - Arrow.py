#TOP SKILL #1: IMPORT PYTHON LIBRARIES (PYTHON CODING)
import requests
from IPython.display import Image, display

#TOP SKILL #2: GET API DATA
getApiData = requests.get("https://coinballer.io/api/technical-indicators-daily/APIKEY")
ApiData = getApiData.json()

#TOP SKILL 3: DECLARE AND SET VARIABLES
#Slice ApiData For Most Recent Date (Today)
ApiData_Today = ApiData[-1]
BollingerUpper = ApiData_Today['bollinger_upper']
BollingerMiddle = ApiData_Today['bollinger_middle']
BollingerLower = ApiData_Today['bollinger_lower']
BitcoinPrice = ApiData_Today['price_close']
BollingerSpread = BollingerUpper - BollingerLower
BollingerPriceSpread = BitcoinPrice - BollingerLower

#TOP SKILL 4: SIMPLE IF STATEMENT
if BitcoinPrice > BollingerUpper:
    BollingerPoints = 100
else: 
  if BitcoinPrice < BollingerLower:
    BollingerPoints = 0
  else: BollingerPoints = round(BollingerPriceSpread / BollingerSpread, 1) * 100

#TOP SKILL #4: SIMPLE IF STATEMENT
if BitcoinPrice > BollingerMiddle:
    Arrow = 'https://i.imgur.com/aCTsoA0.png'
else: Arrow = 'https://i.imgur.com/8Li7d4A.png'

#SHOW SCOREBOARD
print("BOLL", BollingerPoints)
display(Image(Arrow, width = 150, height = 150))
