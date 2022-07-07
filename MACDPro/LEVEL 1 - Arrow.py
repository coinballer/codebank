#TOP SKILL #1: IMPORT PYTHON LIBRARIES (PYTHON CODING)
import requests
from IPython.display import Image, display

#TOP SKILL #2: GET API DATA
getApiData = requests.get("https://coinballer.io/api/macd-pro/APIKEY")
ApiData = getApiData.json()

#TOP SKILL 3: DECLARE AND SET VARIABLES
#Slice ApiData For Most Recent Date (Today)
ApiData_Today = ApiData[-1]
MACDPoints = ApiData_Today['points']

#TOP SKILL #4: SIMPLE IF STATEMENT
if MACDPoints > 50:
    Arrow = 'https://i.imgur.com/aCTsoA0.png'
else: Arrow = 'https://i.imgur.com/8Li7d4A.png'

#SHOW SCOREBOARD
print("MACD Pro Points", MACDPoints)
display(Image(Arrow, width = 150, height = 150))
