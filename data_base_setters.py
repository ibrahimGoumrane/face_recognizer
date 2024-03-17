import mysql.connector as sq
from mysql.connector import Error
from datetime import datetime, timedelta,date
import math
from data_base import system
from utils import utils



class DataBaseSetters:
    def __init__(self) -> None:
        self.db = system

    def set_student_data(self, student_name: str, class_id: int) -> None:
        qwery = "INSERT INTO students (student_name, class_id) VALUES (%s, %s)"
        try:
            self.db.set_qwery(qwery, (student_name, class_id))
        except Error as e:
            print(f"An error occurred during student {student_name} initialization: {e}")
    
    def set_teacher_data(self, teacher_name: str) -> None:
        qwery = "INSERT INTO teachers (teacher_name) VALUES (%s)"
        try:
            self.db.set_qwery(qwery, (teacher_name,))
        except Error as e:
            print(f"An error occurred during teacher {teacher_name} initialization: {e}")

    def set_class_data(self, cycle: str, annee: int, filiere: str) -> None:
        qwery = "INSERT INTO class (cycle, cycle_year, filiere) VALUES (%s, %s, %s)"
        try:
            self.db.set_qwery(qwery, (cycle, annee, filiere))
        except Error as e:
            print(f"An error occurred during class initialization: {e}")


    def set_seance_data(self, class_id: int, module_id: int,date:datetime=datetime.now()) -> None:
        Date_info=utils.set_current_time(date)

        qwery = "INSERT INTO seance (class_id, module_id, start_hour, end_hour, week_day, full_date) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            self.db.set_qwery(qwery, (class_id, module_id, Date_info['start_hour'], Date_info['end_hour'], Date_info['week_day'], Date_info['full_date']))
        except Error as e:
            print(f'An error occurred during seance initialization: {e}')

    def set_module_data(self, class_ID: int, module_name: str, teacher_id: int) -> None:
        qwery = "INSERT INTO module (class_id, module_name, teacher_id) VALUES (%s, %s, %s)"
        try:
            self.db.set_qwery(qwery, (class_ID, module_name, teacher_id))
            print("Module data inserted successfully.")
        except Error as e:
            print(f"An error occurred: {e}")

    #########################dynamique methods
    def set_student_state(self,student_id:int,seance_id:int,state:bool=False)->None: 
        
        qwery='''
        insert  into presence(student_id,seance_id,state) values(%s,%s,%s)
        '''
        try:
            self.db.set_qwery(qwery, (student_id, seance_id, state))
            print("student data inserted successfully.")
        except Error as e:
            print(f"An error occurred: {e}")

            
data_base_setter=DataBaseSetters()