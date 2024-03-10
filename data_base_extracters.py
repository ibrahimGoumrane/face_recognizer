import mysql.connector as sq
from mysql.connector import errorcode
from datetime import date
import numpy as np
from data_base import system

class Data_Base_extracters :
    def __init__(self) -> None:
        self.db=system

    def __get_student_id(self,teacher_name:str)->int :
        pass   
    def __get_teacher_id(self,student_name)->int:
        pass    

    def get_students_class(self,class_id:int)->np.ndarray:
        pass
    def get_class_absence_list(self,class_id:int,date:date)->np.ndarray:
        pass
    def get_student_weekly_global_absence_hours(self,student_id:int,week:date)->dict:
        pass
    def get_student_weekly_module_absence_hours(self,student_id:int,week:date,module_id:int)->dict:
        pass
    def get_student_Absence_status_based_module(self,student_id:int,module_id:int)->dict:    
        pass
