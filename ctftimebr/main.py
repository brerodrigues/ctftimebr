#!/usr/bin/env python3

import time
import ctftimeapi
import config
from models.dbhelper import DbHelper

def main():
    api_url = config.API_URL

    db = DbHelper('sqlite.db')

    ctftime = ctftimeapi.CtftimeApi(api_url)
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


main()