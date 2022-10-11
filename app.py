
from dbhelpers import conn_exe_close
from apihelpers import get_display_results, verify_endpoints_info
from flask import Flask, request, make_response
import json

app = Flask(__name__)

@app.post('/api/hero')
def add_hero():
    invalid = verify_endpoints_info(request.json, ['name','description','image_url'])
    if(invalid != None):
        return make_response(json.dumps(invalid , default=str),400)
    results_json = get_display_results('call add_hero(?,?,?)',[request.json.get('name'),request.json.get('description'),request.json.get('image_url')])
    return results_json

@app.post('/api/villian')
def add_villian():
    invalid = verify_endpoints_info(request.json,['name','description','image_url','hero_id'])
    if(invalid != None):
        return make_response(json.dumps(invalid, default=str),400)
    results_json = get_display_results('call add_villian(?,?,?,?)',
    [request.json.get('name'),request.json.get('description'),request.json.get('image_url'),request.json.get('hero_id')])
    return results_json


@app.get('/api/villian')
def all_villians_for_a_hero():
    invalid = verify_endpoints_info(request.args, ['hero_id'])
    if(invalid != None):
        return make_response(json.dumps(invalid,default=str),400)
    results_json = get_display_results('call all_villians_for_a_hero(?)',[request.args.get('hero_id')])
    return results_json

@app.get('/api/hero')
def all_heros():
    results_json = get_display_results('call all_heros()',[])
    return results_json

app.run(debug=True)
