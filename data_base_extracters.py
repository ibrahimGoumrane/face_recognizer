import mysql.connector as sq
from mysql.connector import errorcode
from datetime import date,datetime
import numpy as np
from data_base import system
from utils import utils
from mysql.connector import Error


class Data_Base_extracters :
    
    def __init__(self) -> None:
        self.db=system

    def get_students_class(self,student_id:int)->np.ndarray:
        qwery='''
                select class_id
                from students
                where  student_id=%s;
            '''
        student_info=self.db.get_qwery(qwery,(student_id))
        return student_info[0]['class_id'] 
   
    def get_seance(self,class_id:int,date:datetime=datetime.now())->np.ndarray:
        Date_info=utils.set_current_time(date)
        qwery = "select seance_id from seance where class_id =%s and start_hour=%s and end_hour=%s and week_day=%s and full_date=%s"
        try:
            seance_info=self.db.get_qwery(qwery, (class_id, Date_info['start_hour'], Date_info['end_hour'], Date_info['week_day'], Date_info['full_date']))
        except Error as e:
            print(f'An error occurred during seance recuperation: {e}')
        return seance_info[0]['seance_id']     
   
    def get_class_absence_list(self,class_id:int,date:datetime=datetime.now())->np.ndarray:
        seance_id=self.get_seance(class_id,date)
        qwery = """
    SELECT students.student_name AS student_name, presence.state AS present
    FROM students 
    JOIN presence ON students.student_id = presence.student_id
    AND presence.seance_id = %s
            """
        try:
            self.db.set_qwery(qwery, (class_id, seance_id))
        except Error as e:
            print(f'Error occurred during class recuperation: {e}')
   
    def get_student_absence_seance_based(self,student_id:int,date:date)->dict:
        class_id=self.get_students_class(student_id)
        Date_info=utils.set_current_time(date)
        qwery='''
        select seance_id from seance 
        where start_hour=%s and end_hour=%s and class_id=%s
        '''
        Seances_ids=self.db.get_qwery(qwery,(Date_info['start_hour'],
                                             Date_info['end_hour'],
                                             class_id))
        student_absence_data=[(seance_id,student_id) for seance_id in Seances_ids]
        qwery='''
        select students.student_name as name , state from students 
        JOIN presence ON students.student_id = presence.student_id 
        where seance_id=%s and students.student_id=%s 
        '''
        absence_state=self.db.get_qwery_many(qwery,student_absence_data)
        return {
            'name':absence_state[0]['name'],
            'sem':[ i+1 for i in range(len(student_absence_data))],
            'start':Date_info['start_hour'],
            'end':Date_info['end_hour'],
            'state':[ state['state'] for state in absence_state ]
        }



    def get_student_weekly_absence_module_based(self,student_id:int,week:date,module_id:int)->dict:
        pass
    def get_student_Absence_status_based_module(self,student_id:int,module_id:int)->dict:    
        pass
