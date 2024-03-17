from data_base_setters import data_base_setter
from datetime import datetime, timedelta,date
import math
##### test to the setters need more improvements 
# data_base_setter.set_class_data('preparatoire',2,'A')
# data_base_setter.set_teacher_data('yassin')
# data_base_setter.set_student_data('ibrahim',1)
# data_base_setter.set_module_data(1, 'Mathématiques',1)
# data_base_setter.set_seance_data(1,1)
# data_base_setter.set_student_state(1,1,True)

Date_Info = datetime.now()
date_v2 =  Date_Info.strftime("%Y-%m-%d")
current_day = Date_Info.weekday()
day_name = (datetime(1900, 1, 1) + timedelta(days=current_day)).strftime('%A')
current_hour = math.floor(Date_Info.hour)

print(date.today())