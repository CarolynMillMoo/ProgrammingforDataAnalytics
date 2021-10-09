#Program which identifies when the current day is Tuesday
# Author: Carolyn Moorhouse

import datetime

print("Let's check if it's Tuesday.")

today = datetime.datetime.today()
dayofweek = today.weekday()

if dayofweek == 1:
    print("It's Tuesday!")
elif dayofweek == 0:
    print("It's not Tuesday.")
    print("Luckily, it will be Tuesday tomorrow!")
else:
    print("Unfortunately it's not Tuesday.")

print("Thanks for checking if it's Tuesday.")