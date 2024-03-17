from datetime import datetime, timedelta,date
from data_base import system
import math

class Utils :

    def __init__(self) -> None:
        self.db=system
    def __get_student_id(self,teacher_name:str)->int :
          pass 
    def __get_teacher_id(self,student_name)->int:
        pass    
    def set_current_time(self,date:datetime=datetime.now())->dict:
        Date_Info = date
        date_v2 =  Date_Info.strftime("%Y-%m-%d")
        current_day = Date_Info.weekday()
        day_name = (datetime(1900, 1, 1) + timedelta(days=current_day)).strftime('%A')
        current_hour = math.floor(Date_Info.hour)
        return {
            'start_hour': current_hour,
            'end_hour': current_hour + 2,
            'week_day': day_name,
            'full_date': date_v2,
        }
    
utils=Utils()
