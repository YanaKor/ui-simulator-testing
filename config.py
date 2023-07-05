'''
Configuration module
'''
import os
import json


BASE_PATH = os.path.dirname(os.path.realpath(__file__))

path = os.path.join(BASE_PATH, "files", "creds.json")

with open(path, 'r') as file:
    creds = json.load(file)


USERNAME = creds['username']
PASSWORD = creds['password']