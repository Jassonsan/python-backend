import psycopg2
from reminder.ReminderCrud import selectAllReminders, selectRangeReminders
from chat.ChatCrud  import selectChatById, createChat

user = "plus57"
password = "Plus57*316"
host = "186.155.209.234"
port = "4719"
database = "plus57db"
def selectAllRemindersI():
    return selectAllReminders(user, password, host, port, database)
def selectRangeRemindersI(since, to):
    return selectRangeReminders(user, password, host, port, database, since, to)
def selectChatByIdI(id):
    return selectChatById(user, password, host, port, database, 842742283)
def createChatI(id, firstname, lastname):
    return createChat(user, password, host, port, database, id, firstname, lastname)
if __name__ == '__main__':
    chat = createChatI(968761100, 'Sergio','Cardenas')
    print(chat)