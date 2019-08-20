#!/usr/bin/env python3

import time
import ctftimeapi
import config
from models.dbhelper import DbHelper

def update_ctf_events():
    api_url = config.API_URL
    ctf_time_url = config.CTF_TIME_URL

    db = DbHelper('sqlite.db')

    ctftime = ctftimeapi.CtftimeApi(api_url, ctf_time_url)
    # get all events from present to end of 2019
    ctf_events = ctftime.get_events_by_time('10000', str(int(time.time())), '1577762809')
    
    db.connect_db()
    db.create_table_events()
    for ctf_event in ctf_events:
        print ('CTF: ' + ctf_event.title)
        print ('Inicio: ' + str(ctf_event.start))
        print ('Fim: ' + str(ctf_event.finish))
        print ('Url: ' + ctf_event.url)
        print ('Duracao ' + ctf_event.duration)
        db.insert_ctf_event(ctf_event)
        print ('-------------------------------------------------') 

def update_ranking_teams():
    api_url = config.API_URL
    ctf_time_url = config.CTF_TIME_URL

    db = DbHelper('sqlite.db')

    ctftime = ctftimeapi.CtftimeApi(api_url, ctf_time_url)
    # get the first 10 ctf br teams
    ctf_br_teams = ctftime.get_br_teams(10)
    db.connect_db()
    db.drop_table_teams() # drop table because i'm too lazy to validade the duplicates
    db.create_table_teams()
    for ctf_team in ctf_br_teams:
        print (ctf_team.name + '-' + str(ctf_team.position) + '-' + str(ctf_team.points))
        db.insert_ctf_team_ranking(ctf_team)

def main():
    update_ctf_events()




main()
