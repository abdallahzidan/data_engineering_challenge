import sqlite3
import pandas as pd

sqliteConnection = sqlite3.connect('db\sqlite.db')

# gets the maximum time stored per each table and return data in dictionary
def get_offset_time(initialLoad):
    offset_dict={}
    # incase of initial load we return 0 offset 
    if(initialLoad):
        return {'metrics':0,'workorder':0}
    
    try:
        sqliteConnection = sqlite3.connect('db\sqlite.db')
        cursor = sqliteConnection.cursor()
        
        #getting max of time and store in offset_dict dictionay 
        max_metrics_query = "select max(time) from metrics"
        max_workorder_query = "select max(time) from workorder"
        cursor.execute(max_metrics_query)
        record = cursor.fetchall()
        offset_dict['metrics']=record[0][0]
        
        cursor.execute(max_workorder_query)
        record = cursor.fetchall()
        offset_dict['workorder']=record[0][0]
        
        print("offset_dict: ", offset_dict)
        cursor.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            return offset_dict
        
# inserts delta data into sqlite database
def insert_batch(json,table):
    try:
        sqliteConnection.open()
    except:
        pass
    print('insert into: ' +table)
    my_json = json.decode('utf8').replace("'", '"')
    df = pd.read_json(my_json)
    df.to_sql(table,sqliteConnection,if_exists='replace',index=False)
    sqliteConnection.commit()
    sqliteConnection.close()
    print(str(len(df))+" records inserted into "+ table)
    
    