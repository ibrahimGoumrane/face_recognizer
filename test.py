from datetime import date
from datetime import datetime,timedelta
import math
current_day = datetime.now().weekday()
print(timedelta(days=current_day))
day_name = (datetime(1900, 1, 1) + timedelta(days=current_day))
print(day_name)
print(math.floor(datetime.now().hour))
print(math.floor(datetime.now().minute))
#datetime.now()
print(datetime.ctime(datetime.now()))