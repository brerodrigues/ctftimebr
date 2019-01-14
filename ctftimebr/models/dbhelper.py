#!/usr/bin/env python3

import sqlite3

class DbHelper(object):
    
    #database = 'sqlite.db'

    def __init__(self, database_location):
        # if dont exists, create db and connect
        self.database = database_location
        self.connect_db()

    def __del__(self):
        self.cursor.close()

    def create_table_events(self):
        events_sql = '''CREATE TABLE events(id INTEGER PRIMARY KEY, 
                    title TEXT, ctf_time_url TEXT, restrictions TEXT, start DATE, finish DATE, 
                    description TEXT, url TEXT, format TEXT, duration TEXT)'''
        try:
            self.cursor.execute(events_sql)
            self.db.commit()
        except sqlite3.OperationalError, e:
            print ('Can\'t create table events')
            print (e)
            self.db.rollback()

    def connect_db(self):
        self.db = sqlite3.connect(self.database)
        self.cursor = self.db.cursor()
        self.db.text_factory = str

    def insert(self, object):
        print ('insert object')

    def insert_ctf_event(self, event):
        id = event.id
        title = event.title
        ctf_time_url = event.ctf_time_url
        restrictions = event.restrictions
        start = event.start
        finish = event.finish
        description = event.description
        url = event.url
        format = event.format
        duration = event.duration

        try:
            self.cursor.execute('''INSERT INTO events(id, title, ctf_time_url,
                                restrictions, start, finish, description,
                                url, format, duration)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (id, title,
                                ctf_time_url, restrictions, start, finish,
                                description, url, format, duration))

            self.db.commit()
        except sqlite3.IntegrityError, e:
            print ('CTF event {} already registred').format(title)
            print (e)
        except Exception as e:
            self.db.rollback()
            raise e

    def list_ctf_events(self):
        self.cursor.execute(''' SELECT * FROM events ORDER BY date(start) ASC''')
        return self.cursor.fetchall()

    def update_ctf_event(self, event):
        print ('update ctf event')
