from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

import routes.alert_route
import routes.user_route

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3222)