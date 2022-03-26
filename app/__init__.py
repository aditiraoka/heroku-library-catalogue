# -*- coding: utf-8 -*-
"""
 Created on Sat Mar 26 12:31:35 2022
 Author: Aditirao Kalanji
 Version: {mayor}.{minor}.{rel}
 Email: aditirao19@gmail.com
 Status: {dev_status}
"""


from app.libs import *
import os,inspect
from flask import Flask

lib_app = Flask(__name__)
lib_app.config['SESSION_TYPE'] = 'filesystem'
lib_app.config['SECRET_KEY']='apple123'
lib_app.config['JWT_SECRET_KEY']='jwt-secret-string'
lib_app.config['CONFIG_FILE']=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

#Initializing JWT App
#jwt = JWTManager(app)


#TO-DO Auth sessions