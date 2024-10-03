from flask import Flask 

app = Flask(__name__)

@app.route("/", methods=('GET',))
def index():
    return "<h1>Pagina Inicial</h1><p>Eu sou o fulano</p>"
    
@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>galeria</h1>"

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>contato</h1>"

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>sobre</h1>"

