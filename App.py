#!usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector

from flask import Flask, render_template, flask, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql_password'
app.config['MYSQL_DB'] = 'mydatabase'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key ='seret123'
    app.run(debug=True)
    
