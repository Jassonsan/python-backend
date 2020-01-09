import psycopg2
from .ChatModel import Chat

def selectChatById(user, password, host, port, database, chatId):
    ret = False
    try:
        connection = psycopg2.connect(user = user, password = password, host = host, port = port, database = database)
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from chat where chat_id = %s"
        where = [chatId]
        cursor.execute(postgreSQL_select_Query, where)
        chats = cursor.fetchall() 
        print('chats ', chats)
        if len(chats) > 0:
            ret = True
    except (Exception, psycopg2.Error) as error :
        print ("Error on selectChatById", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    return ret
def createChat(user, password, host, port, database, chatId, firstname, lastname):
    if selectChatById(user, password, host, port, database, chatId):
        return False
    else:
        try:
            connection = psycopg2.connect(user = user, password = password, host = host, port = port, database = database)
            cursor = connection.cursor()
            postgreSQL_insert_Query = "insert into chat values (%s, %s, %s)"
            values = (chatId, firstname, lastname)
            cursor.execute(postgreSQL_insert_Query, values)
            connection.commit()
            ret = True
        except (Exception, psycopg2.Error) as error :
            print ("Error on createChat", error)
            ret = False
        finally:
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
        return ret
