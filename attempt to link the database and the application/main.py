
from sqlite3 import Cursor
import pymysql 
from config import host, user, password,db_name 


def add(Description : str, user_ID : int ) : 

    try : 
        connection  = pymysql.connect( 
            host = host, 
            port = 3306 ,
            user = user ,
            password = password, 
            database= db_name, 
            cursorclass= pymysql.cursors.DictCursor
        )
        print("succesfully connected...")
        print("#" * 20)
        try  : 
            with connection.cursor() as cursor : 
            
                task_id = 0
                cursor.execute("SELECT MAX(task_id) as maximum from task")
                task_id = cursor.fetchall()
                for i in task_id : 
                    task_id = int(i['maximum']) 
                if(task_id == None ): 
                    task_id = 1 
                else : 
                    task_id += 1 
                insert_query = "INSERT INTO task value(" + str(task_id) + ", '" +  Description + "' ,"  + str(user_ID) + ")"
                print(insert_query)
                cursor.execute(insert_query)
                connection.commit()
                print('Insert succesfull')      
        finally : 
            connection.close()  
    except Exception as ex : 
        print("connection refused...")
        print("connection ex")
def print_base(user_ID : int ) : 
    try : 
        connection  = pymysql.connect( 
            host = host , 
            port = 3306 ,
            user = user ,
            password = password, 
            database = db_name, 
            cursorclass= pymysql.cursors.DictCursor
        )
        print("succesfully connected...")
        print("#" * 20)
        try  : 
            with connection.cursor() as cursor :
                cursor.execute("select * from task where " + str(user_ID) + " = person_ID" ) 
                task_id = cursor.fetchall() 
        finally : 
            connection.close()  
            return task_id 
    except Exception as ex : 
        print("connection refused...")
        print("connection ex")
def authentification(nickname : str, user_password : str , registration : bool ) : #- отрицательный номер - в случае ошибки, положительный номер - ИД пользователя 
    try : 
        connection  = pymysql.connect( 
            host = host , 
            port = 3306 ,
            user = user ,
            password = password, 
            database = db_name, 
            cursorclass= pymysql.cursors.DictCursor
        )
        print ("Seccesfuly conncted") 
        print ("#" * 20 ) 
        if registration == True : 
            try  : 
                with connection.cursor() as cursor :
                    cursor.execute("select Nickname from person")
                    users = cursor.fetchall() 
                    for i in users : 
                        if i['Nickname'] == nickname : 
                            result =  -1 # Сообщение об ошибке "Пользователь с таким именем уже существует
                            return result
                    cursor.execute("SELECT MAX(Person_ID) as maximum from person")
                    person_ID = cursor.fetchall()[0]['maximum'] + 1 
                    Request = "INSERT INTO person value ( " +str(person_ID) + ", '" + str(nickname) + "', '" + str(user_password) + "')"
                    cursor.execute(Request  )
                    connection.commit()
                    print('Registration succesfull') 
            except Exception as ex : 
                print("registration failed") 
            finally : 
                connection.close()  
        else : #Блок авторизации 
            try : 
                with connection.cursor() as cursor : 
                    cursor.execute("select * from person") 
                    users = cursor.fetchall() 
                    for i in users : 
                        if i['Nickname'] == nickname : 
                            if i['password'] == user_password : 
                                result = i['Person_ID']
                                break 
                        else : 
                            result = -2 #Пользователь с таким именем не найден 
            finally : 
                connection.close()  
                return result 
    except Exception as ex : 
            print ("connecion refused ") 
            print ("connceion ex") 
