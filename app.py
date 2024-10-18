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

@app.route("/area/<float:largura>/<float:comprimento>",methods=('GET',))
def area(largura: float, comprimento: float):
    
    return f"""<h1>A área informada é l={largura} * a={comprimento} Area={largura*comprimento} <h1>"""

    @app.route("/par/<float:numero>", methods=('GET',))
    def par(numero : float):
        
        if numero % 2 ==0:
            return "<p> O numero é par<p>"
        
        if numero is None:
            return "<p>Digite um numero válido<p>"

        else:
            return "<p>O numero é impar<p>"


@app.route("/potencial/<int:n1>/<int:n2>", methods=('GET',))
def potencial(n1: float, n2: float):
    return f"""<h1>O primeiro numero {n1} elevado ao segundo numero {n2} é igual a {n1**n2} <h1>"""

@app.route("/tabuada/<float:numero>",methods=('GET',))
def tabuada(numero: float):
    if numero > 0:
        return f"""<p>A tabuada do numero {numero}:<p>
        <ul><li><p> {numero} * 1 = {numero*1} </p></ul></li>
        <ul><li><p> {numero} * 2 = {numero*2} </p></ul></li> 
        <ul><li><p> {numero} * 3 = {numero*3} </p></ul></li> 
        <ul><li><p> {numero} * 4 = {numero*4} </p></ul></li> 
        <ul><li><p> {numero} * 5 = {numero*5} </p></ul></li> 
        <ul><li><p> {numero} * 6 = {numero*6} </p></ul></li> 
        <ul><li><p> {numero} * 7 = {numero*7} </p></ul></li> 
        <ul><li><p> {numero} * 8 = {numero*8} </p></ul></li> 
        <ul><li><p> {numero} * 9 = {numero*9} </p></ul></li> 
        <ul><li><p> {numero} * 10 = {numero*10} </p></ul></li>
        """
    
    else:
        return "<p>Digite um número válido</p>"



 
    

    


