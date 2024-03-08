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

    def __init__(self) -> None:  
        self.__Create_Database()
        self.__User_Base_Connection(SGDA.Db_name)
        self.__Creating_Table(Tables.TABLES)
        self.__Close_Connection() 
   
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
                        database=DataBase)
            self.cursor=self.cnx.cursor()
        except sq.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("wrong User name or password")
            else:
                print(err)
               
    def __Create_Database(self):
        self.__User_Base_Connection()
        try:
            self.cursor.execute(
                "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(SGDA.Db_name)
            )
        except sq.Error as err:
            print("Failed creating database: {}".format(err))  

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

    

if  __name__=="__main__":
    system=SGDA()

