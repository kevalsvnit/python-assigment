import pandas as pd
from datetime import datetime, time

# a) Timestamp for a specific date
dt1 = pd.Timestamp('2012-01-15')
print("a) DateTime object for Jan 15 2012:", dt1)

# b) Timestamp for specific date and time
dt2 = pd.Timestamp('2012-01-15 21:20:00')
print("b) Specific date and time of 9:20 PM:", dt2)

# c) Current local datetime
dt3 = pd.Timestamp.now()
print("c) Local date and time:", dt3)

# d) Date part only
dt4 = dt3.date()
print("d) A date without time:", dt4)

# e) Current date
dt5 = pd.to_datetime("today").date()
print("e) Current date:", dt5)

# f) Time part only
dt6_time = dt3.time()
print("f) Time from a datetime:", dt6_time)

# g) Current local time
dt7 = datetime.now().time()
print("g) Current local time:", dt7)
