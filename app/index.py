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
    list_of_hashes = sheet.get_all_records()
    total=len(list_of_hashes)
    read, tbr,reviewed = 0,0,0
    for i in range(0,total):
        if list_of_hashes[i]['Status'] == "Read":
            read=read+1
        if list_of_hashes[i]['Blog Link'] != "NA":
            reviewed=reviewed+1

    tbr=total-read

    return render_template("home.html", read=read, reviewed=reviewed, total=total, tbr=tbr )

@lib_app.route("/books", methods=['GET','POST'])
def show_books():
    list_of_hashes = sheet.get_all_records()
    return render_template("list_books.html", result=list_of_hashes, length=len(list_of_hashes))