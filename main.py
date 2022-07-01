import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data 

ticker = 'SPY'
start = '10-09-2002'
end = '30-06-2022'
data = pandas_datareader.data.DataReader(ticker, 'yahoo', start, end)

day_returns = [1]
for day in range(1,len(data)):
  day_return = data['Close'][day] / data['Open'][day]
  day_returns.append(day_returns[day-1]*day_return)

for i in range(len(data)):
  day_returns[i] = (day_returns[i]-1)*100

daynight_returns = [1]
for daynight in range(1,len(data)):
  daynight_return = data['Adj Close'][daynight] / data['Adj Close'][daynight-1]
  daynight_returns.append(daynight_returns[daynight-1]*daynight_return)

for i in range(len(data)):
  daynight_returns[i] = (daynight_returns[i]-1)*100

plt.figure(facecolor='white')
plt.plot(data.index, daynight_returns, label='Day and Night Returns')
plt.plot(data.index, day_returns, label='Day Returns')
plt.ylabel("Returns (%)")
plt.title('$'+ticker+' Percentage Returns from '+start+' until '+end)
plt.legend(loc="upper left")
ax = plt.axes()
ax.set_facecolor("white")
plt.show()
