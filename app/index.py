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

def get_status_books(status):
    list_of_hashes = sheet.get_all_records()
    length=len(list_of_hashes)
    result=[]
    for i in range(0,length):
        if status == "Read" or status == "TBR":
            if list_of_hashes[i]['Status'] == status:
                result.append(list_of_hashes[i])
        elif status == "Reviewed":
            if list_of_hashes[i]['Blog Link'] != "NA":
                result.append(list_of_hashes[i])
    return result

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
def list_books():
    list_of_hashes = sheet.get_all_records()
    #return render_template("list_books.html", result=list_of_hashes, length=len(list_of_hashes))
    return render_template("page.html", result=list_of_hashes, length=len(list_of_hashes), status="All")

@lib_app.route("/read", methods=['GET', 'POST'])
def list_read():
    read=get_status_books("Read")
    return render_template("page.html", result=read, length=len(read), status="Read")

@lib_app.route("/tbr", methods=['GET', 'POST'])
def list_tbr():
    tbr=get_status_books("TBR")
    return render_template("page.html", result=tbr, length=len(tbr), status="To Be Read")

@lib_app.route("/reviewed", methods=['GET', 'POST'])
def list_reviewed():
    review=get_status_books("Reviewed")
    return render_template("page.html", result=review, length=len(review), status="Reviewed")