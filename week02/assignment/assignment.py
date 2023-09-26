"""
Course: CSE 251 
Lesson Week: 02
File: assignment.py 
Author: Brother Comeau

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py"
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the decription of the assignment.
  Note that the names are sorted.
- You are requied to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a seperate
  file for the class)
- Do not add any global variables except for the ones included in this program.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.

{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}
"""

from datetime import datetime, timedelta
import requests
import json
import threading

# Include cse 251 common Python files
from cse251 import *

# Const Values
TOP_API_URL = r'http://127.0.0.1:8790'

# Global Variables
call_count = 0


# TODO Add your threaded class definition here
class Request_thread(threading.Thread):
    # https://realpython.com/python-requests/
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}
    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.response = response.json()
        else:
            print('RESPONSE = ', response.status_code)

# TODO Add any functions you need here


def main():
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')
    reqF6 = requests.get(f'{TOP_API_URL}/films/6')
    responseF6 = json.loads(reqF6.text)
    fTitle = responseF6["title"]
    fDirector = responseF6["director"]
    fProducer = responseF6["producer"]
    fDate = responseF6["release_date"]
    fChars = responseF6["characters"]
    fPlanets = responseF6["planets"]
    fShips = responseF6["starships"]
    fVehicles = responseF6["vehicles"]
    fRaces = responseF6["species"]

    log.write('-----------------------------------------')
    log.write(f'Title   : {fTitle}')
    log.write(f'Director: {fDirector}')
    log.write(f'Producer: {fProducer}')
    log.write(f'Released: {fDate}')
    log.write()
    log.write(f'Characters: {len(fChars)}')
    fCharList = str
    for i in responseF6["characters"]:
      req = requests.get(i)
      response = json.loads(req.text)
      fCharList = (f'{fCharList} {response["name"]}, ')
    log.write(fCharList)
    log.write()
    log.write(f'Planets: {len(fPlanets)}')
    fCharList = ''
    for i in responseF6["planets"]:
      req = requests.get(i)
      response = json.loads(req.text)
      fCharList = (f'{fCharList} {response["name"]}, ')
    log.write(fCharList)
    log.write()
    log.write(f'Starships: {len(fShips)}')
    fCharList = ''
    for i in responseF6["starships"]:
      req = requests.get(i)
      response = json.loads(req.text)
      fCharList = (f'{fCharList} {response["name"]}, ')
    log.write(fCharList)
    log.write()
    log.write(f'Vehicles: {len(fVehicles)}')
    fCharList = ''
    for i in responseF6["vehicles"]:
      req = requests.get(i)
      response = json.loads(req.text)
      fCharList = (f'{fCharList} {response["name"]}, ')
    log.write(fCharList)
    log.write()
    log.write(f'Species: {len(fRaces)}')
    fCharList = ''
    for i in responseF6["species"]:
      req = requests.get(i)
      response = json.loads(req.text)
      fCharList = (f'{fCharList} {response["name"]}, ')
    log.write(fCharList)
    log.write()
    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')
    

if __name__ == '__main__':

    response = requests.get(TOP_API_URL)
    
    # Check the status code to see if the request succeeded.
    if response.status_code == 200:
        main()
    else:
        print('Error in requesting ID')