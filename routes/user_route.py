from decouple import config 
from flask import Flask, request, json
#from flask_api import status
from flask_cors import CORS, cross_origin
from include.validators import parsedRespond, hasErrorMsg, parsedRespondUser
from src.user.infrastructure.controller import UserController


from __main__ import app


CORS(app)

@cross_origin

#http://localhost:3222/api/v1/user?user=bryan&pasw=1234
@app.route('%s%s/%s' % (config('API_PATH'), config('API_VERSION'),  'login'), methods=["GET"])
def seek_users():
    try:
        _userCL = UserController()
        print("------------------------1")
        data = _userCL.buscarUsuario(request.args['user'],request.args['pass'])
        print("------------------------2")
        return parsedRespondUser(data)
    except Exception as err:
        return hasErrorMsg(err)
