import mysql.connector as sq
from mysql.connector import errorcode
from tables import Tables

#SGA system de gestion d'absence

class SGDA:
    '''
    admin local host has all the privilege  of an administrator on a MySQL server. 
    this class should handle database and table creation on its own.
    '''
    Db_name='SGDA'
    __user='admin'
    __pasword='admin'
    __instance=None
    
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SGDA, cls).__new__(cls)
        return cls.__instance  
    
    def __init__(self) -> None:  
        #commented  lines are for database initialisation purpose only
        #self.__Create_Database()
        self.__User_Base_Connection(SGDA.Db_name)
        #self.__Creating_Table(Tables.TABLES)
        #self.__Delete_DataBase() #experiments
        #self.__Close_Connection() 
        
    def __User_Base_Connection(self,DataBase='')->None:
        try :
            if DataBase :
                self.cnx = sq.connect(user=SGDA.__user,
                                        password=SGDA.__pasword,
                                        host='localhost',
                                        database=DataBase)
            else :    
                self.cnx = sq.connect(user=SGDA.__user,
                        password=SGDA.__pasword,
                        host='localhost',
                        )
            self.cursor=self.cnx.cursor()
            self.get_cursor=self.cnx.cursor(dictionary=True)
        except sq.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("wrong User name or password")
            else:
                print(err)
        self.cnx.commit()       
    
    def __Create_Database(self):
        self.__User_Base_Connection()
        try:
            self.cursor.execute(
                "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(SGDA.Db_name)
            )
        except sq.Error as err:
            print("Failed creating database: {}".format(err))  
        self.cnx.commit()
    
    def __Close_Connection(self):
        self.cursor.close()
        self.cnx.close()

    def __Creating_Table(self ,table:dict):
            for table_name in table:
                table_description = table[table_name]
                try:
                    print("Creating table {}: ".format(table_name), end='')
                    self.cursor.execute(table_description)
                except sq.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        print("already exists.")
                    else:
                        print(err.msg)
                        self.cnx.rollback()
                else:
                    print('created') 
            self.cnx.commit()
            print("finished")
   
    def __Delete_DataBase(self):
        self.cursor.execute('DROP DATABASE IF EXISTS {};'.format(SGDA.Db_name))
    
    #data manipulation queries
    def set_qwery(self,query:str,data:tuple)->None:
        self.__User_Base_Connection(DataBase=SGDA.Db_name)
        self.cursor.execute(query, data)
        self.cnx.commit()
        self.__Close_Connection()
    
    def set_qwery_many(self,query:str,data:list[tuple])->None:
        try:
            # Execute the query for each set of values
            for person_data in data:
                self.set_qwery(query,person_data)
            # Commit the changes
            print("Records inserted successfully.")

        except sq.Error as err:
            print(f"Error: {err}")
        self.__Close_Connection()    
    
    def get_qwery(self,query:str)->list[dict]:
        self.__User_Base_Connection(DataBase=SGDA.Db_name)
        self.get_cursor.execute(query)
            # Fetch all rows as dictionaries (column names will be keys)
        values:list[dict]=self.get_cursor.fetchall()
        self.__Close_Connection()
        return values


system = SGDA()