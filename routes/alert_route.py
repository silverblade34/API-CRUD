from decouple import config 
from flask import Flask, request, json
#from flask_api import status
from flask_cors import CORS, cross_origin
from include.validators import parsedRespond, hasErrorMsg
from src.alert.infrastructure.controller import AlertsController

#-- Prueba conexion mysql

from __main__ import app


CORS(app)

@cross_origin

#http://localhost:3222/api/v1/user?user=bryan&pasw=1234
@app.route('%s%s/%s' % (config('API_PATH'), config('API_VERSION'),  'list/alerts'), methods=["GET"])
def list_alerts():
    try:
        _alertCL = AlertsController()
        data = _alertCL.listarAlertas()
        return parsedRespond(data)
    except Exception as err:
        return hasErrorMsg(err)

@app.route('%s%s/%s' % (config('API_PATH'), config('API_VERSION'),  'seek/alert'), methods=["GET"])
def seek_alert():
    try:
        _alertCL = AlertsController()
        data = _alertCL.buscarAlertas(request.args['id'])
        return parsedRespond(data)
    except Exception as err:
        return hasErrorMsg(err)

@app.route('%s%s/%s' % (config('API_PATH'), config('API_VERSION'),  'edit/alert'), methods=["PUT"])
def edit_alert():
    try:
        _alertCL = AlertsController()
        data = _alertCL.editarAlertas(request.json['id'], request.json['evento'],request.json['descripcion'],request.json['placa'],request.json['estado'])
        return parsedRespond(data)
    except Exception as err:
        return hasErrorMsg(err)

@app.route('%s%s/%s' % (config('API_PATH'), config('API_VERSION'),  'create/alert'), methods=["POST"])
def create_alert():
    try:
        _alertCL = AlertsController()
        data = _alertCL.crearAlertas(request.json['evento'],request.json['descripcion'],request.json['placa'],request.json['estado']) 
        return parsedRespond(data)
    except Exception as err:
        return hasErrorMsg(err)

@app.route('%s%s/%s' % (config('API_PATH'), config('API_VERSION'),  'delete/alert'), methods=["DELETE"])
def delete_alert():
    try:
        _alertCL = AlertsController()
        data= _alertCL.eliminarAlertas(request.json['id'])  
        return parsedRespond(data)
    except Exception as err:
        return hasErrorMsg(err)