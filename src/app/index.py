# -*- coding: utf-8 -*-
"""
 Created on Sat Mar 26 12:45:41 2022
 Author: Aditirao Kalanji
 Version: {mayor}.{minor}.{rel}
 Email: aditirao19@gmail.com
 Status: {dev_status}
"""
from app import lib_app
from app.libs import * 
import sqlite3 as sql
from flask import render_template


@lib_app.route('/',methods=['GET', 'POST'])
def hello_world():
    return "<h1>Hello World!</h1>"