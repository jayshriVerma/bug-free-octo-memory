import matplotlib.pyplot as plt 
import pandas as pd 
import mplfinance as mpl 
import yfinance
import datetime
import yfinance as yf

#define the ticker symbol Microsoft
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
start=datetime.datetime(2020,1,1)
end=datetime.datetime.now()

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start=start,end=end)

#see your data
#print(tickerDf)
#print(tickerData.info)
#print(tickerData.recommendations)
#print(tickerData.calendar)
#using matplotlib
#plt.plot(tickerDf['Close'])
#plt.show()
#adding our own styles
colors=mpl.make_marketcolors(up="green",down="red",edge="black",wick="black",volume="blue")
custom_style=mpl.make_mpf_style(marketcolors=colors)
#Now plotting using mplfinance
mpl.plot(tickerDf,type="renko",style=custom_style,mav=(3,6,9),renko_params=dict(brick_size="atr",atr_length=2),volume=True,show_nontrading=True)
#print(mpl.available_styles())
mpl.plot(tickerDf,type="pnf",style=custom_style,mav=(3,6,9),pnf_params=dict(box_size=1.5,atr_length=2),volume=True)