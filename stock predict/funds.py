import pandas as pd
import numpy as np
import plotly.graph_objects as go
import datareturn 

df=datareturn.datas("AAPL") #Getting the alphavantage LIVE data
df=pd.DataFrame(df)
fig=go.Figure(data=[go.Candlestick(x=df[df.columns[0]],
open=df['1. open'],
high=df['2. high'],
low=df['3. low'],
close=df['4. close'])])
fig.update_layout(
    title="Plot Title",
    xaxis_title="DATE",
    yaxis_title="PRICE",
    legend_title="STOCK PREDICTOR",
    font=dict(family="Courier New, monospace",size=18,color="Black")
)

fig.show()