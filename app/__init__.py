from flask import Flask
from flaskext.mysql import MySQL
from flask_cors import CORS
from itsdangerous import TimedJSONWebSignatureSerializer  as Serializer




app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config["SECRET_KEY"] = "12345678"

mysql = MySQL(app)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'votaciones'
app.config['MEDIA_DIR'] = "./static/img"
mysql.init_app(app)

token_serializer = Serializer(app.config.get("SECRET_KEY"),expires_in=28000)

from app.api.v1 import api
apiResource = api


