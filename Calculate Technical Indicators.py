#TOP SKILL 1: IMPORT PYTHON LIBRARIES (PYTHON CODING)
#Import Python Libraries
!pip install pandas
!pip install requests
!pip install stockstats
import requests
import pandas as pandas
from stockstats import StockDataFrame

#TOP SKILL 2: GET API DATA
getApiData = requests.get("https://coinballer.io/api/pro-weekly/APIKEY")
ApiData = getApiData.json()

#TOP SKILL 3: DECLARING VARIABLES (EMPTY BOXES)
open = []
close = []
high = []
low = []
volume = []
amount = []

#TOP SKILL 2: SETTING VARIABLES WITH A BASIC LOOP (FILL THE EMPTY BOXES)
for i in ApiData:
    iprice_open = i['price_open']
    open.append(iprice_open)
    iprice_close = i['price_close']
    close.append(iprice_close)
    iprice_high = i['price_high']
    high.append(iprice_high)
    iprice_low = i['price_low']
    low.append(iprice_low)
    ivolume = i['volume']
    volume.append(ivolume)
    amount.append(ivolume)

YourDataFrame = pandas.DataFrame({
    'open': open,
    'close': close,
    'high': high,
    'low': low,
    'volume': volume,
    'amount': amount,            
})

#CALCULATE TECHNICAL INDICATORS: (RSI, BOLLINGER BANDS, MACD, WLPR, MOVING AVERAGES)
#RSI: YourIndicator['rsi_14'] = YourIndicator.get('rsi_14')
#BOLL: YourIndicator['boll'] = YourIndicator.get('boll')
#MACD: YourIndicator['macd'] = YourIndicator.get('macd')
#WLPR: YourIndicator['wr'] = YourIndicator.get('wr')
#MA 200: YourIndicator['close_200_sma'] = YourIndicator.get('close_200_sma')
#MA 200: YourIndicator['close_100_sma'] = YourIndicator.get('close_100_sma')
#MA 200: YourIndicator['close_50_sma'] = YourIndicator.get('close_50_sma')
YourIndicator = StockDataFrame.retype(YourDataFrame)
YourIndicator['rsi_14'] = YourIndicator.get('rsi_14')

#SHOW TECHNICAL INDICATOR DATA
print(YourIndicator)
