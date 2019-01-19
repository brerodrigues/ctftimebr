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
        except sqlite3.OperationalError:
            print ('Can\'t create table events')
            #print (e)
            self.db.rollback()

    def create_table_teams(self):
        teams_sql = '''CREATE TABLE teams(id INTEGER PRIMARY KEY, 
                name TEXT, position INTEGER, points REAL)'''
        try:
            self.cursor.execute(teams_sql)
            self.db.commit()
        except sqlite3.OperationalError:
            print ('Can\'t create table teams')
            #print (e)
            self.db.rollback()

    def drop_table_teams(self):
        teams_sql = '''DROP TABLE teams'''
        try:
            self.cursor.execute(teams_sql)
            self.db.commit()
        except sqlite3.OperationalError:
            print ('Can\'t drop table teams')
            #print (e)
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
        except sqlite3.IntegrityError:
            print ('CTF event {} already registred').format(title)
            # print (e)
        except Exception as e:
            self.db.rollback()
            raise e

    def list_ctf_events(self):
        self.cursor.execute(''' SELECT * FROM events ORDER BY date(start) ASC''')
        return self.cursor.fetchall()

    def list_ctf_events_by_limit(self, limit):
        sql = ''' SELECT * FROM events where finish > date('now') 
                ORDER BY date(start) ASC LIMIT {}'''.format(limit)
        print (sql)
        self.cursor.execute(sql)

        return self.cursor.fetchall()

    def update_ctf_event(self, event):
        print ('update ctf event')

    def insert_ctf_team_ranking(self, team):
        name = team.name
        position = team.position
        points = team.points

        try:
            self.cursor.execute('''INSERT INTO teams(name, position, points)
                                VALUES(?, ?, ?)''', (name, position, points))

            self.db.commit()
        except sqlite3.IntegrityError:
            print ('Team {} already registred').format(name)
            # print (e)
        except Exception as e:
            self.db.rollback()
            raise e

    def list_ctf_teams_by_position(self):
        self.cursor.execute(''' SELECT * FROM teams ORDER BY (position) ASC''')
        return self.cursor.fetchall()
