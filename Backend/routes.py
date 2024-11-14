import pandas as pd
from json import loads, dumps
import pyodbc

#Databestand importeren
gmet = pd.read_csv("gmet.csv")


def init_gmet_route():
    @app.route("/gmet100")
    def start():
        eerste = gmet.head(100)
        result = eerste.to_json(orient="records")
        parsed = loads(result)
        print(jaar)
        return dumps(parsed, indent=4)



