# -*- coding: utf-8 -*-
"""
 Created on Sat Mar 26 12:45:41 2022
 Author: Aditirao Kalanji
 Version: {mayor}.{minor}.{rel}
 Email: aditirao19@gmail.com
 Status: {dev_status}
"""
from app import lib_app, list_of_hashes
from app.libs import * 
import sqlite3 as sql
from flask import render_template


@lib_app.route('/',methods=['GET', 'POST'])
def hello_world():
    return render_template("index.html")

@lib_app.route("/books", methods=['GET','POST'])
def show_books():

    return render_template("list.html", result=list_of_hashes, length=len(list_of_hashes))