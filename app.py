from flask import (Flask,request) 

app = Flask(__name__)

@app.route("/", methods=('GET',))
def index():
    nome = request.args.get('nome')
    return f"""<h1>Pagina Inicial</h1>
    <p>Olá {nome}, que nome bonito
    """
    
@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>galeria</h1>"

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>contato</h1>"

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>sobre</h1>"

@app.route("/area")
def area():
    altura=float(request.args.get('a'))
    largura=float(request.args.get('l'))
    return f"""<h1>A área informada l={largura} * a={altura} Area={largura*altura} <h1>"""

    @app.route("/par", methods=('GET',))
    def par():
        numero = int (request.args.get('n'))
        
        if numero % 2 ==0:
            return "<p> O numero é par<p>"
        
        if numero is None:
            return "<p>Digite um numero válido<p>"

        else:
            return "<p>O numero é impar<p>"


@app.route("/nome", methods=('GET',))
    def nome():
        n = request.args.get('n')
        s = request.args.get('s')
        return f"""<p>{n}, {s}<p>"""
 
    

    


