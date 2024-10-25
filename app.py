from flask import (Flask, render_template, request) 

app = Flask(__name__)

@app.route("/", methods=('GET',))
def index():
    nome = request.args.get('nome')
    return f"""<h1>Pagina Inicial</h1>
    <p>Olá {nome}, que nome bonito
           <ul><h3>Menu</h3>
            <li><a href="/">Index</a></li>
            <li><a href="/tabuada/10.0">Tabuada</a></li>
            <li><a href="/sobre">Sobre</a></li>
            <li><a href="/contato">Contato</a></li>
            <li><a href="/galeria">Galeria</a></li>
            <li><a href="/area/10.0/10.0">Àrea</a></li>
            <li><a href="/potencial/3/3">Potencial</a></li>
            <li><a href="/par/3.0">ImparPar</a></li>
        </ul>
    """
    
@app.route("/galeria", methods=('GET',))
def galeria():
    return """<h1>galeria</h1>
            <ul><h3>Menu</h3>
            <li><a href="/">Index</a></li>
            <li><a href="/tabuada/10.0">Tabuada</a></li>
            <li><a href="/sobre">Sobre</a></li>
            <li><a href="/contato">Contato</a></li>
            <li><a href="/galeria">Galeria</a></li>
            <li><a href="/area/10.0/10.0">Àrea</a></li>
            <li><a href="/potencial/3/3">Potencial</a></li>
            <li><a href="/par/3.0">ImparPar</a></li>
        </ul>
    """

@app.route("/contato", methods=('GET',))
def contato():
    return """<h1>contato</h1>
            <ul><h3>Menu</h3>
            <li><a href="/">Index</a></li>
            <li><a href="/tabuada/10.0">Tabuada</a></li>
            <li><a href="/sobre">Sobre</a></li>
            <li><a href="/contato">Contato</a></li>
            <li><a href="/galeria">Galeria</a></li>
            <li><a href="/area/10.0/10.0">Àrea</a></li>
            <li><a href="/potencial/3/3">Potencial</a></li>
            <li><a href="/par/3.0">ImparPar</a></li>
        </ul>
    """

@app.route("/sobre", methods=('GET',))
def sobre():
    return """<h1>sobre</h1>
            <ul><h3>Menu</h3>
            <li><a href="/">Index</a></li>
            <li><a href="/tabuada/10.0">Tabuada</a></li>
            <li><a href="/sobre">Sobre</a></li>
            <li><a href="/contato">Contato</a></li>
            <li><a href="/galeria">Galeria</a></li>
            <li><a href="/area/10.0/10.0">Àrea</a></li>
            <li><a href="/potencial/3/3">Potencial</a></li>
            <li><a href="/par/3.0">ImparPar</a></li>
        </ul>
    """

@app.route("/area/<float:largura>/<float:comprimento>",methods=('GET',))
def area(largura: float, comprimento: float):
    
    return f"""<h1>A área informada é l={largura} * a={comprimento} Area={largura*comprimento} <h1>
            <ul><h3>Menu</h3>
            <li><a href="/">Index</a></li>
            <li><a href="/tabuada/10.0">Tabuada</a></li>
            <li><a href="/sobre">Sobre</a></li>
            <li><a href="/contato">Contato</a></li>
            <li><a href="/galeria">Galeria</a></li>
            <li><a href="/area/10.0/10.0">Àrea</a></li>
            <li><a href="/potencial/3/3">Potencial</a></li>
            <li><a href="/par/3.0">ImparPar</a></li>
        </ul>
    """

@app.route("/par/<float:numero>", methods=('GET',))
def  par(numero : float):
        
    if numero % 2 ==0:
        return """<p> O numero é par<p>
            <ul><h3>Menu</h3>
            <li><a href="/">Index</a></li>
            <li><a href="/tabuada/10.0">Tabuada</a></li>
            <li><a href="/sobre">Sobre</a></li>
            <li><a href="/contato">Contato</a></li>
            <li><a href="/galeria">Galeria</a></li>
            <li><a href="/area/10.0/10.0">Àrea</a></li>
            <li><a href="/potencial/3/3">Potencial</a></li>
            <li><a href="/par/3.0">ImparPar</a></li>
        </ul>
        """
        
    if numero is None:
        return """<p>Digite um numero válido<p>
            <ul><h3>Menu</h3>
            <li><a href="/">Index</a></li>
            <li><a href="/tabuada/10.0">Tabuada</a></li>
            <li><a href="/sobre">Sobre</a></li>
            <li><a href="/contato">Contato</a></li>
            <li><a href="/galeria">Galeria</a></li>
            <li><a href="/area/10.0/10.0">Àrea</a></li>
            <li><a href="/potencial/3/3">Potencial</a></li>
            <li><a href="/par/3.0">ImparPar</a></li>
        </ul>
        """

    else:
        return """<p>O numero é impar<p>
            <ul><h3>Menu</h3>
            <li><a href="/">Index</a></li>
            <li><a href="/tabuada/10.0">Tabuada</a></li>
            <li><a href="/sobre">Sobre</a></li>
            <li><a href="/contato">Contato</a></li>
            <li><a href="/galeria">Galeria</a></li>
            <li><a href="/area/10.0/10.0">Àrea</a></li>
            <li><a href="/potencial/3/3">Potencial</a></li>
            <li><a href="/par/3.0">ImparPar</a></li>
        </ul>
        """


@app.route("/potencial/<int:n1>/<int:n2>", methods=('GET',))
def potencial(n1: float, n2: float):
    return f"""<h1>O primeiro numero {n1} elevado ao segundo numero {n2} é igual a {n1**n2} <h1>
            <ul><h3>Menu</h3>
            <li><a href="/">Index</a></li>
            <li><a href="/tabuada/10.0">Tabuada</a></li>
            <li><a href="/sobre">Sobre</a></li>
            <li><a href="/contato">Contato</a></li>
            <li><a href="/galeria">Galeria</a></li>
            <li><a href="/area/10.0/10.0">Àrea</a></li>
            <li><a href="/potencial/3/3">Potencial</a></li>
            <li><a href="/par/3.0">ImparPar</a></li>
        </ul>
    """

@app.route("/tabuada")
@app.route("/tabuada/<float:numero>",methods=('GET',))
def tabuada(numero = None): 

    if 'numero' in request.args:
        numero = request.args.get('numero')
    return render_template('tabuada.html', numero=numero)

@app.route("/juros")
@app.route("/juros/<capital>/<juros>/<anos>/<aporte>",methods=('GET',))
def juros(capital = None, juros = None, anos = None, aporte = None): 

    if 'capital' in request.args:
        capital = request.args.get('capital')
        capital = float (request.args.get('capital'))

    if 'juros' in request.args:
        juros = request.args.get('juros')
        juros = float (request.args.get('juros'))

    if 'anos' in request.args:
        anos = request.args.get('anos')
        anos = float (request.args.get('anos'))

    if 'aporte' in request.args:
        aporte = request.args.get('aporte')
        aporte = float (request.args.get('aporte'))
    
    return render_template('juros.html', capital=capital, anos=anos, juros=juros, aporte=aporte)

@app.route("/login")
def login(email = None, senha = None): 
    if 'email' and 'senha' in request.args:
        email = request.args.get('email')
        senha = request.args.get('senha')

    return render_template('login.html', email=email, senha=senha)
    





 
    

    


