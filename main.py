import datetime
import schedule
import sqlite3 as sql
import time
import winsound
import threading

"""
TO DO:

ADD IMPORT FROM XLSX TEMPLATE FEATURE
"""

# This Function deletes all entries on the DB and stops all scheduled alarms


def clean():
    schedule.clear()
    connect = sql.connect('events3.db')
    cursor = connect.cursor()
    cursor.execute(f"SELECT * FROM EVENTS")
    for element in cursor.fetchall():
        task = list(element)
        cursor.execute(f"""delete from EVENTS where ID='{task[0]}'""")
    connect.commit()
    connect.close()
    return 0


# This Function loads data from the local db


def load_db():
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    saturday = []
    sunday = []
    connect = sql.connect('events3.db')
    cursor = connect.cursor()
    cursor.execute(f"SELECT * FROM EVENTS")

    for element in cursor.fetchall():
        task = list(element)
        if task[1] == 'Monday':
            monday.append(task)
        elif task[1] == 'Tuesday':
            tuesday.append(task)
        elif task[1] == 'Wednesday':
            wednesday.append(task)
        elif task[1] == 'Thursday':
            thursday.append(task)
        elif task[1] == 'Friday':
            friday.append(task)
        elif task[1] == 'Saturday':
            saturday.append(task)
        elif task[1] == 'Sunday':
            sunday.append(task)
    connect.close()
    return monday, tuesday, wednesday, thursday, friday, saturday, sunday


# PLAYS SIREN


def alarm():
    print('ALARM!')


# get current day name


def today():
    now = datetime.datetime.now()
    return now.strftime("%A")


# this function removes the alarm from db and schedule


def kill(id):
    job = schedule.get_jobs(f"t{id}")
    schedule.cancel_job(job[0])
    c = sql.connect('events3.db')
    cur = c.cursor()
    cur.execute(f"""delete from EVENTS where ID='{id}'""")
    c.commit()
    c.close()
    return 0


# this function adds the alarm from db and schedule


def add(day, time, description='PAS DE DESCRIPTION'):
    c = sql.connect('events3.db')
    cur = c.cursor()
    cur.execute(f"INSERT INTO EVENTS(DAY, START_TIME, DESCRIPTION) VALUES ('{day}','{time}', '{description}')")
    lastadded = cur.execute(f"SELECT * FROM EVENTS where ID={cur.lastrowid}")

    lastadded = list(lastadded)
    lastadded = lastadded[0]
    if lastadded[1] == 'Monday':
        schedule.every().monday.at(lastadded[2]).do(alarm).tag(f"t{lastadded[0]}")
    elif lastadded[1] == 'Tuesday':
        schedule.every().tuesday.at(lastadded[2]).do(alarm).tag(f"t{lastadded[0]}")
    elif lastadded[1] == 'Wednesday':
        schedule.every().wednesday.at(lastadded[2]).do(alarm).tag(f"t{lastadded[0]}")
    elif lastadded[1] == 'Thursday':
        schedule.every().thursday.at(lastadded[2]).do(alarm).tag(f"t{lastadded[0]}")
    elif lastadded[1] == 'Friday':
        schedule.every().friday.at(lastadded[2]).do(alarm).tag(f"t{lastadded[0]}")
    elif lastadded[1] == 'Saturday':
        schedule.every().saturday.at(lastadded[2]).do(alarm).tag(f"t{lastadded[0]}")
    elif lastadded[1] == 'Sunday':
        schedule.every().sunday.at(lastadded[2]).do(alarm).tag(f"t{lastadded[0]}")

    c.commit()
    c.close()
    return 0


def initialize():
    schedule.clear()
    monday, tuesday, wednesday, thursday, friday, saturday, sunday = load_db()

    for day in monday:
        schedule.every().monday.at(day[2]).do(alarm).tag(f"t{day[0]}")
        print(f"t{day[0]}")
    for day in tuesday:
        schedule.every().tuesday.at(day[2]).do(alarm).tag(f"t{day[0]}")
    for day in wednesday:
        schedule.every().wednesday.at(day[2]).do(alarm).tag(f"t{day[0]}")
    for day in thursday:
        schedule.every().thursday.at(day[2]).do(alarm).tag(f"t{day[0]}")
    for day in friday:
        schedule.every().friday.at(day[2]).do(alarm).tag(f"t{day[0]}")
    for day in saturday:
        schedule.every().saturday.at(day[2]).do(alarm).tag(f"t{day[0]}")
    for day in sunday:
        schedule.every().sunday.at(day[2]).do(alarm).tag(f"t{day[0]}")

    all_jobs = schedule.get_jobs()
    print(all_jobs)

    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    add('Sunday', '02:16')
    threading.Thread(target=initialize).start()
    all_jobs = schedule.get_jobs()
    print(len(all_jobs))
    #add('Saturday', '20:11', 'buh')
    all_jobs = schedule.get_jobs()
    print(len(all_jobs))


main()

"""
all_jobs = schedule.get_jobs()
print(all_jobs)
kill(35)
"""

#add("Thursday", "03:54", "TESTING")





