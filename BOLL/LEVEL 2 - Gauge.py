#TOP SKILL #1: IMPORT PYTHON LIBRARIES (PYTHON CODING)
import requests
from IPython.display import Image, display

#TOP SKILL #2: GET API DATA
getApiData = requests.get("https://coinballer.io/api/macd-pro/APIKEY")
ApiData = getApiData.json()

#TOP SKILL 3: DECLARE AND SET VARIABLES
#Slice ApiData For Most Recent Date (Today)
ApiData_Today = ApiData[-1]
BollingerUpper = ApiData_Today['points']
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
    GaugeColor = 'green'
else: GaugeColor = 'red'

#TOP SKILL: CREATE A CHART USING PLOTLY
Gauge = plotly.express.bar(x=["BOLL Points"], y=[BollingerPoints], text=[BollingerPoints], labels={
                     "x": "",
                     "y": "BOLL Points",
                 })
Gauge.update_traces(marker_color=GaugeColor)
Gauge.update_layout(yaxis_range=[0,100], plot_bgcolor='white', width=300, height=500)
Gauge.update_xaxes(visible=True,showticklabels=False)

#SHOW SCOREBOARD
Gauge.show()
