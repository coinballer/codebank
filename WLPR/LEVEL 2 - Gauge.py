#TOP SKILL 1: IMPORT PYTHON LIBRARIES (PYTHON CODING)
import requests
from IPython.display import Image, display
import plotly.express

#TOP SKILL 2: GET API DATA
getApiData = requests.get("https://coinballer.io/api/pro-daily/APIKEY")
ApiData = getApiData.json()

#TOP SKILL 3: DECLARE AND SET VARIABLES
#Slice ApiData For Most Recent Date (Today)
ApiData_Today = ApiData[-1]
WLPR = ApiData_Today['wlpr']
WLPRPoints = 100 + ApiData_Today['wlpr']

#TOP SKILL 4: SIMPLE IF STATEMENT
if WLPR > -50:
    GaugeColor = 'green'
else: GaugeColor = 'red'

#TOP SKILL: CREATE A CHART USING PLOTLY
Gauge = plotly.express.bar(x=["WLPR Points"], y=[WLPRPoints], text=[WLPRPoints], labels={
                     "x": "",
                     "y": "WLPR Points",
                 })
Gauge.update_traces(marker_color=GaugeColor)
Gauge.update_layout(yaxis_range=[0,100], plot_bgcolor='white', width=300, height=500)
Gauge.update_xaxes(visible=True,showticklabels=False)

#SHOW SCOREBOARD
Gauge.show()
