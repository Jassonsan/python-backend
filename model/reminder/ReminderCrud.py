import psycopg2
from reminder.ReminderModel import Reminder

def selectAllReminders(user, password, host, port, database):
    ret = []
    try:
        connection = psycopg2.connect(user = user, password = password, host = host, port = port, database = database)
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from reminder"
        cursor.execute(postgreSQL_select_Query)
        reminders = cursor.fetchall() 
        for rem in reminders:
            reminder = Reminder(rem[0], rem[1], rem[2], rem[3], rem[4])
            ret.append(reminder)
    except (Exception, psycopg2.Error) as error :
        print ("Error on selectAllReminders", error)
        return None
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    return ret

def selectRangeReminders(user, password, host, port, database, since, to):
    ret = []
    try:
        connection = psycopg2.connect(user = user, password = password, host = host, port = port, database = database)
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from reminder where day between %s and %s"
        where = (since, to)
        cursor.execute(postgreSQL_select_Query, where)
        reminders = cursor.fetchall() 
        for rem in reminders:
            reminder = Reminder(rem[0], rem[1], rem[2], rem[3], rem[4])
            ret.append(reminder)
    except (Exception, psycopg2.Error) as error :
        print ("Error on selectAllReminders", error)
        return None
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    return ret


            

