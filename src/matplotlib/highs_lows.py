import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename='sitka_weather_2014.csv'
highs,dates,lows = [],[],[]
with open(filename) as f:
    reader = csv.reader(f)
    headrow = next(reader)
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        # print(current_date)
        highs.append(int(row[1]))
        lows.append(int(row[2]))
print(highs)
print(dates)

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',linewidth='0.3')
plt.plot(dates,lows,c='blue',linewidth='0.3')
plt.fill_between(dates,highs,lows,color='blue',alpha=0.1)
fig.autofmt_xdate()
plt.show()



# print(headrow)
#
# for index,c in enumerate(headrow):
#     print(index,c)

# highs = []
# for row in reader:
#     highs.append(row[1])
#
# print(highs)