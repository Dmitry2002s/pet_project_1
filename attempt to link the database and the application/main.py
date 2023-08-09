
import pymysql 
from config import host, user, password,db_name 


def add(Description : str) : 

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
                Person_ID = 1 
                insert_query = "INSERT INTO task value(" + str(task_id) + ", '" +  Description + "' ,"  + str(Person_ID) + ")"
                print(insert_query)
                cursor.execute(insert_query)
                connection.commit()
                print('Insert succesfull')      
        finally : 
            connection.close()  
    except Exception as ex : 
        print("connection refused...")
        print("connection ex")
def print_base() : 
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
                cursor.execute("select * from task") 
                task_id = cursor.fetchall() 
        finally : 
            connection.close()  
            return task_id 
    except Exception as ex : 
        print("connection refused...")
        print("connection ex")
