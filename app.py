from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola mi amor preciosa,solo te queria decir que estoy muy orgulloso de ti y que te amo mucho muackkk"
