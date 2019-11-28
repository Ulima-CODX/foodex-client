import requests
import json


def getclienteprofile(id):
    payload = {'id': id}
    response = requests.get('https://us-central1-foodex-backend.cloudfunctions.net/client_profile', params=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def getdishesbymenu(id):
    payload = {'menu_id': id}
    response = requests.get('https://us-central1-foodex-backend.cloudfunctions.net/dishes', params=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def getdish(id):
    payload = {'id': id}
    response = requests.get('https://us-central1-foodex-backend.cloudfunctions.net/dishes', params=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def getestablishments():
    response = requests.get('https://us-central1-foodex-backend.cloudfunctions.net/establishments')
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def getestablishment(id):
    payload = {'id': id}
    response = requests.get('https://us-central1-foodex-backend.cloudfunctions.net/establishments', params=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def getordersbyclient(id):
    payload = {'client_id': id}
    response = requests.get('https://us-central1-foodex-backend.cloudfunctions.net/orders', params=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def getorder(id):
    payload = {'id': id}
    response = requests.get('https://us-central1-foodex-backend.cloudfunctions.net/orders', params=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def setorder(id,data):
    payload = {'id': id}
    response = requests.post('https://us-central1-foodex-backend.cloudfunctions.net/orders', params=payload,data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def getreservationbyclient(id):
    payload = {'client_id': id}
    response = requests.get('https://us-central1-foodex-backend.cloudfunctions.net/reservations', params=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {}

def getreservation(id):
    payload = {'id': id}
    response = requests.get('https://us-central1-foodex-backend.cloudfunctions.net/reservations', params=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def setservation(id,data):
    payload = {'id': id}
    response = requests.get('https://us-central1-foodex-backend.cloudfunctions.net/reservations', params=payload,data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        return {}