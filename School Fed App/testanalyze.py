import time
from analysis import analyze
analyze()

print("pause")
time.sleep(2)

from pypltmonths import plotGraphTotalSpentPerMonth
from pypltdates.py import plotGraphTotalSpentPerDay
plotGraphTotalSpentPerMonth()
plotGraphTotalSpentPerDay()
