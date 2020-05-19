#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:02:26 2020

@author: ing
"""
from flask import Flask, escape, request, make_response
import each
import celan
import json
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__)
app.config['CORS_HEADER'] = 'Content-Type'
# cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:5000"}})


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/count_each_product_stock')
def getcountEachProductStock():
    data = each.countEachProductStock()
    resp = make_response(json.dumps(data))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/predict_celan',methods=['GET'])
def getcountpredict_regLineaire():
    equipe = request.args.get('equipe')
    annee = request.args.get('annee')
    data = celan.predict_regLineaire(equipe,annee)
    resp = make_response(json.dumps(data))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
