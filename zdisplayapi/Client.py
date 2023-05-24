import requests
import json


class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        # Initialisez ici d'autres variables nécessaires pour l'interaction avec l'API
    
    def get_user_by_email(self, email):
        data = {
            'key': self.api_key,
            'method' : 'get_user_by_email',
            'email' : email
        }

        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}

        response = requests.get(url="https://zdisplay.fr/api/", data=json_data, headers=headers)

        if response.status_code != 200:
            return response.status_code, data, response.json()['error']

        return response.status_code, data, response.json()
    
    def get_users(self):
        data = {
            'key': self.api_key,
            'method' : 'get_users',
        }

        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}

        response = requests.get(url="https://zdisplay.fr/api/", data=json_data, headers=headers)

        if response.status_code != 200:
            return response.status_code, data, response.json()['error']

        return response.status_code, data, response.json()