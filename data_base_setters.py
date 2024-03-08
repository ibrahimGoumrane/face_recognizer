import mysql.connector as sq
from mysql.connector import errorcode
from datetime import datetime, timedelta,date
import math
from data_base import system

class DataBaseSetters:
    def __init__(self) -> None:
        self.db = system

    def set_student_data(self, student_name: str, class_id: int) -> None:
        query = "INSERT INTO students (Name, ClassID) VALUES (?, ?)"
        try:
            system.set_query(query, (student_name, class_id))
        except errorcode.MySQLConnectorError as e:
            print(f"An error occurred during student {student_name} initialization: {e}")

    def set_teacher_data(self, teacher_name: str) -> None:
        query = "INSERT INTO teachers (teacher_name) VALUES (?)"
        try:
            system.set_query(query, (teacher_name,))
        except errorcode.MySQLConnectorError as e:
            print(f"An error occurred during teacher {teacher_name} initialization: {e}")

    def set_class_data(self, cycle: str, annee: int, section: str) -> None:
        query = "INSERT INTO class (cycle, cycle_year, section) VALUES (?, ?, ?)"
        try:
            system.set_query(query, (cycle, annee, section))
        except errorcode.MySQLConnectorError as e:
            print(f"An error occurred during class initialization: {e}")

    def set_seance_data(self, class_id: int, module_id: int) -> None:
        Date_Info = datetime.now()
        date_v2 = Date_Info.strftime("%m/%d/%Y")
        current_day = Date_Info.weekday()
        day_name = (datetime(1900, 1, 1) + timedelta(days=current_day)).strftime('%A')
        current_hour = math.floor(Date_Info.hour)
        Date_info = {
            'start_hour': current_hour,
            'end_hour': current_hour + 2,
            'week_day': day_name,
            'full_date': date_v2,
        }

        query = "INSERT INTO class (class_id, module_id, start_hour, end_hour, week_day, full_date) VALUES (?, ?, ?, ?, ?, ?)"
        try:
            system.set_query(query, (class_id, module_id, Date_info['start_hour'], Date_info['end_hour'], Date_info['week_day'], Date_info['full_date']))
        except errorcode.MySQLConnectorError as e:
            print(f'An error occurred during class initialization: {e}')

    def set_module_data(self, class_ID: int, module_name: str, teacher_id: int) -> None:
        query = "INSERT INTO modules (class_id, module_name, teacher_id) VALUES (?, ?, ?)"
        try:
            system.set_query(query, (class_ID, module_name, teacher_id))
            print("Module data inserted successfully.")
        except errorcode.MySQLConnectorError as e:
            print(f"An error occurred: {e}")

    #########################dynamique methods
    def set_student_present(self,student_id:int,Date_Info:date)->None: 
        pass   
    def set_student_absent(self,student_id:int,Date_Info:date)->None: 
        pass    