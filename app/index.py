# -*- coding: utf-8 -*-
"""
 Created on Sat Mar 26 12:45:41 2022
 Author: Aditirao Kalanji
 Version: {mayor}.{minor}.{rel}
 Email: aditirao19@gmail.com
 Status: {dev_status}
"""
from app import lib_app, sheet
from app.libs import * 
from flask import render_template


@lib_app.route('/',methods=['GET', 'POST'])
def hello_world():
    return render_template("index.html")

@lib_app.route("/books", methods=['GET','POST'])
def show_books():
    list_of_hashes = sheet.get_all_records()
    return render_template("list.html", result=list_of_hashes, length=len(list_of_hashes))