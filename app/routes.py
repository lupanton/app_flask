# -*- coding: utf-8 -*- 
from flask import *
from app import app

@app.route('/')
def index():
    user = {'username': 'Anton'}
    return render_template('index.html', title='Home', user=user)