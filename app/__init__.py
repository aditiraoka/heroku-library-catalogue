# -*- coding: utf-8 -*-
"""
 Created on Sat Mar 26 12:31:35 2022
 Author: Aditirao Kalanji
 Version: {mayor}.{minor}.{rel}
 Email: aditirao19@gmail.com
 Status: {dev_status}
"""


from pyparsing import col
from app.libs import *
import os,inspect
from flask import Flask

import gspread
from oauth2client.service_account import ServiceAccountCredentials

lib_app = Flask(__name__)

lib_app.config['SESSION_TYPE'] = 'filesystem'
lib_app.config['SECRET_KEY']='apple123'
lib_app.config['JWT_SECRET_KEY']='jwt-secret-string'
lib_app.config['CONFIG_FILE']=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("My Books").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()

#Initializing JWT App
#jwt = JWTManager(app)


#TO-DO Auth sessions