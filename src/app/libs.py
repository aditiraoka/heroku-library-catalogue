# -*- coding: utf-8 -*-
"""
 Created on Sat Mar 26 12:32:42 2022
 Author: Aditirao Kalanji
 Version: {mayor}.{minor}.{rel}
 Email: aditirao19@gmail.com
 Status: {dev_status}
"""

#Flask imports

from flask import Flask, jsonify, flash, session, logging, redirect, url_for, render_template, Response
#from flask_restful import reqparse
import sqlite3 as sql

#General import
import re, os, sys, getopt, operator