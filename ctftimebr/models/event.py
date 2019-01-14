#!/usr/bin/env python3

import json
import pytz # http://benalexkeen.com/working-with-timezones-in-python/
from datetime import datetime # https://chrisalbon.com/python/basics/strings_to_datetime/ 

class Event(object):
    
    def __init__(self, event_json):
        event_dict = json.loads(event_json)
        self.id = event_dict['id']
        self.ctf_time_url = str(event_dict['ctftime_url'])
        self.title = str(event_dict['title'].encode('utf-8'))
        self.restrictions = str(event_dict['restrictions'])
        #self.organizers = event_dict['organizers']
        self.start = str(self.get_br_date_time(event_dict['start']))
        self.finish = str(self.get_br_date_time(event_dict['finish']))
        self.description = str(event_dict['description'].encode('utf-8'))
        self.url = str(event_dict['url'])
        self.format = event_dict['format']
        self.duration = self.get_duration(event_dict['duration'])

    def get_br_date_time(self, date_time):
        date_time_splited = date_time.split('T')
        date = date_time_splited[0] + '-'
        time = date_time_splited[1].split(':')[0] + ':' + date_time_splited[1].split(':')[1]
        date_time_formated = datetime.strptime(date + time, '%Y-%m-%d-%H:%M')
        
        br_timezone = pytz.timezone('America/Recife')
        utc_timezone = pytz.timezone('UTC')
        date_time_formated_utc = utc_timezone.localize(date_time_formated)
        br_date_time = br_timezone.normalize(date_time_formated_utc)
        #YYYY-MM-DD HH:MM:SS.SSS
        #br_date_time = datetime.strftime(br_date_time, '%d/%m/%Y %H:%M')
        br_date_time = datetime.strftime(br_date_time, '%Y-%m-%d %H:%M')
        
        return br_date_time

    def get_duration(self, duration):
        return (str(duration['days']) + ' dias ' + str(duration['hours']) + ' horas')