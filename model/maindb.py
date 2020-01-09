import psycopg2
from reminder.ReminderCrud import selectAllReminders, selectRangeReminders

user = "plus57"
password = "Plus57*316"
host = "186.155.209.234"
port = "4719"
database = "plus57db"
def selectAllRemindersI():
    return selectAllReminders(user, password, host, port, database)
def selectRangeRemindersI(since, to):
    return selectRangeReminders(user, password, host, port, database, since, to)
if __name__ == '__main__':
    records = selectAllRemindersI()
    for record in records:
        print(record.reminderId)
    print('/n END /n')
    records = selectRangeRemindersI(14, 20)
    for record in records:
        print(record.reminderId)