#!/usr/bin/env python3

import json
import requests
from models.team import Team
from models.event import Event

class CtftimeApi(object):
    
    events_endpoint = 'events/?'
    event_endpoint = 'events/'
    teams_endpoint = 'teams/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def __init__(self, api_url):
        self.api_url = api_url

    def get_events_by_time(self, limit, start_date, end_date):
        request_url = self.get_endpoint_url(self.events_endpoint) + \
                        'limit=' + limit + '&start=' + start_date + '&finish=' + end_date + '/'

        response = requests.get(request_url, headers=self.headers)
        events_json = json.loads(response.content) # converting to list of dicts
        events_list = []

        for event_json in events_json:
            event = Event(json.dumps(event_json)) # converting dict to str before create object
            events_list.append(event)
            
        return events_list

    def get_event(self, event_id):
        request_url = self.get_endpoint_url(self.event_endpoint) + event_id + '/'
        response = requests.get(request_url, headers=self.headers)

        if response.status_code == 200:
            event_json = response.content
            event = Event(response.content)
            return event

        return self.get_request_error(response)

    def get_team(self, team_id):
        print ('get team information')

    def get_endpoint_url(self, endpoint):
        # check if url has a / in the end?
        url = self.api_url + endpoint
        return url

    def get_request_error(self, request_response):
        default_message = 'There\'s a error in the api request, code: '
        status_code = str(request_response.status_code)

        return default_message + status_code