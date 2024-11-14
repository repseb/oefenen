from flask import Flask
from flask import render_template
from flask_cors import CORS

#Importeer functie uit routes.py
from routes import init_gmet_route

app = Flask(__name__)
cors = CORS(app)

init_gmet_routes(app)

