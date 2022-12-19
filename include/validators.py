from flask import json, jsonify
from flask_api import status


def parsedRespond(data):
    temp = {
        'data': data[0],
        'message': data[1],
        'status': True
    }
    return jsonify(temp)

def parsedRespondUser(data):
    temp = {
        'data': data[0],
        'status': True
    }
    return jsonify(temp)

def hasErrorMsg(err):
    temp = {
        'message': str(err),
        'status': False
    }

    return jsonify(temp), status.HTTP_400_BAD_REQUEST