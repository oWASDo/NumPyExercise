"""
Wind Statistics
----------------

Topics: Using numArrays methods over different axes, fancy indexing.

1. The data in 'wind.data' has the following format::

        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71

   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   locations in Ireland on that day.

   Use the 'loadtxt' function from numpy to read the data into
   an numArrays.

2. Calculate the min, max and mean windspeeds and standard deviation of the
   windspeeds over all the locations and all the times (a single set of numbers
   for the entire dataset).

3. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds at each location over all the days (a different set of numbers
   for each location)

4. Calculate the min, max and mean windspeed and standard deviations of the
   windspeeds across all the locations at each day (a different set of numbers
   for each day)

5. Find the location which has the greatest windspeed on each day (an integer
   column number for each day).

6. Find the year, month and day on which the greatest windspeed was recorded.

7. Find the average windspeed in January for each location.

You should be able to perform all of these operations without using a for
loop or other looping construct.

Bonus
~~~~~

1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months. (hint: first find a
   way to create an identifier unique for each month. The second step might
   require a for loop.)

2. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds across all locations for each week (assume that the first week
   starts on January 1 1961) for the first 52 weeks. This can be done without
   any for loop.

Bonus Bonus
~~~~~~~~~~~

Calculate the mean windspeed for each month without using a for loop.
(Hint: look at `searchsorted` and `add.reduceat`.)

Notes
~~~~~

These data were analyzed in detail in the following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.


See :ref:`wind-statistics-solution`.
"""

from numpy import loadtxt
import numpy as np
import numpy.ma as ma
from colorama import Fore, Back, Style
import colorama
import calendar

print("")
colorama.init()
numArrays = loadtxt("wind.data")

dates = numArrays[:, :3]
dates.astype(int)
numData = numArrays[:, 3:]

mainTextColor = Fore.RED
valueColor = Fore.YELLOW

print(mainTextColor + "Max temperature for all data: ")
print(valueColor + "%f C°" % numData.max())
print(mainTextColor + "Min temperature for all data: ")
print(valueColor + "%f C°" % numData.min())
print(mainTextColor + "Avarage of temperatures for all data: ")
print(valueColor + "%f C°" % numData.mean())
print(mainTextColor + "Standart deviation of temperatures for all data: ")
print(valueColor + "%f C°" % numData.std())
print("")

print(mainTextColor + "Value for each location:")
print("MAX:" + valueColor)
print(numData.max(axis=0))
print(mainTextColor + "MIN:" + valueColor)
print(numData.min(axis=0))
print(mainTextColor + "AVARAGE:" + valueColor)
print(numData.mean(axis=0))
print(mainTextColor + "STANDERD DEVIATION:" + valueColor)
print(numData.std(axis=0))
print("")

print(mainTextColor + "Value for on day in all loacation:")
print("MAX:" + valueColor)
print(numData.max(axis=1))
print(mainTextColor + "MIN:" + valueColor)
print(numData.min(axis=1))
print(mainTextColor + "AVARAGE:" + valueColor)
print(numData.mean(axis=1))
print(mainTextColor + "STANDARD DEVIATION:" + valueColor)
print(numData.std(axis=1))
print("")

print(mainTextColor + "Num of all location: ")
print("MAX:" + valueColor)
print(numData.argmax(axis=1))
print("")

print(mainTextColor + "Day of max recorded temeperature:" + valueColor)
maxTempIndex = numData.argmax() // 12
print("Years: %i" % dates[maxTempIndex, 0])
print("Month: %i" % dates[maxTempIndex, 1])
print("Day: %i" % dates[maxTempIndex, 2])
print("")

months = dates[:, 1]
index = np.argwhere(months == 1)
print(mainTextColor + "Avarage on January for each location:" + valueColor)
print(numData[index].mean(axis=0))

print(mainTextColor + "Avarage for each maonth:" + valueColor)

days = dates[:, 2]
daysCopy = np.copy(days)
daysCopy = np.roll(daysCopy, -1)

daysIndex = np.argwhere(daysCopy < days)

startIndex = 0
endIndex = daysIndex[0]
endIndex = endIndex.item(0)
cicleIndex = 0
while True:
   try:
      array = numData[startIndex : endIndex + 1, :]
      print(mainTextColor + "date:" + valueColor)
      print(dates[startIndex, :2])
      print(array.mean())
      cicleIndex += 1
      startIndex = daysIndex[cicleIndex]
      startIndex = startIndex.item(0)
      endIndex = daysIndex[cicleIndex +1 ].astype(int)
      endIndex = endIndex.item(0)
      print()
   except:
      print()
      array = numData[startIndex : , :]
      print(mainTextColor + "date:" + valueColor)
      print(dates[startIndex, :2])
      print(array.mean())
      break

#print(np.arange(12*6574).reshape(6574, 12))

