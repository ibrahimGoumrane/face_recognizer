import mysql.connector as sq
from mysql.connector import errorcode
from datetime import date
import numpy as np
from data_base import system


class Data_Base_Setters :
    def __init__(self) -> None:
        self.db=system 
    #adding data to database methods
    def set_student_data(self,student_name:str,class_id:int)->None:
        pass
    def set_teacher_data(self,teacher_name:str)->None:
        pass
    def set_class_data(self,cycle:str,annee:int,section:str)->None:
        pass
    def set_seance_data(self,class_id:int,Date_Info:date,module_id:int)->None:
        pass
    def set_module_data(self,class_ID:int,module_name:str,teacher_id:int)->None:
        pass

    #########################dynamique methods
    def set_student_present(self,student_id:int,Date_Info:date)->None: 
        pass   
    def set_student_absent(self,student_id:int,Date_Info:date)->None: 
        pass    