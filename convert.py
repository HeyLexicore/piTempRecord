import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import re

#plt.style.use('_mpl-gallery-nogrid')


def currday(time):
    current_datetime = datetime.fromtimestamp(time)
    day_of_year = current_datetime.timetuple().tm_yday
    if day_of_year == 340:
        print(time)
    return day_of_year
def currminute(time):
    current_datetime = datetime.fromtimestamp(time)
    hour = current_datetime.timetuple().tm_hour
    minute = current_datetime.timetuple().tm_min


    return hour+minute/60

f = open("time.csv","r")
lines = re.sub(r"[^0-9,.]","",f.read()[:-1]).replace("\n",",").split(",")
f.close()
print(lines)
time = [float(x) for i,x in enumerate(lines) if np.mod(i,2)==0]
temp = [float(x) for i,x in enumerate(lines) if np.mod(i,2)==1]

x = [currday(x) for x in time]
y = [currminute(x) for x in time]
z = temp
print(x,y,z)
"""z.append(0)
z.append(0)
z.append(0)
z.append(0)

x.append(0)
y.append(0)

x.append(356)
y.append(0)

x.append(0)
y.append(1440)

x.append(356)
y.append(1440)
"""




levels = np.linspace(min(z), max(z),50)

# plot:
fig, ax = plt.subplots()

#ax.plot(x, y, 'o', markersize=2, color='grey')
ax.tricontourf(x, y, z, levels=levels)

ax.set(xlim=(0, 357), ylim=(24, 0))
fig.set_size_inches(16/3,9/3)
plt.show()