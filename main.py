from flask import Flask
from datetime import datetime
import pytz

moscowTz = pytz.timezone("Europe/Moscow") 
timeInMoscow = datetime.now(moscowTz)
currentTimeInMoscow = timeInMoscow.strftime("%H:%M:%S")

app = Flask(__name__)

@app.route("/")
def hello():
    return ("Hello World! Time is " + currentTimeInMoscow)

if __name__ == '__main__':
    app.run(debug = True)
    app.reload()