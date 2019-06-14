import quandl
import pandas as pd
import matplotlib.pyplot as plt

class tes:
	def plot_brand(self,num):
		q = quandl.get("TSE/"+num)
		q.to_csv('data/csv/tse'+num+'.csv')

		stock = pd.read_csv('data/csv/tse'+num+'.csv')
		stock['100MA'] = stock['Close'].rolling(window = 100,min_periods=0).mean()
		stock['200MA'] = stock['Close'].rolling(window = 200, min_periods=0).mean()

		fig = plt.figure()
		axes = fig.add_axes([0.1,0.1,0.8,0.8])
		axes.plot(stock['Close'][-365:], 'black', lw = 1)
		axes.plot(stock['100MA'][-365:])
		axes.plot(stock['200MA'][-365:])
		axes.set_xlabel('Time')
		axes.set_ylabel('Price')
		axes.set_title(num+' 1 Year')
		axes.legend()

		plt.show()

