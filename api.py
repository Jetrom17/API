from flask import Flask, render_template, jsonify, redirect

app = Flask(__name__)

# Dicionário como fonte de dados
dados = {
    'titulo': 'Playlist',
    'conteudo': 'Os links foram encontrados na internet de forma pública!',
    'informacoes': {
        'link1': 'https://superflixapi.top/',
        'link2': 'https://warezstream.net/',
        'link3': 'https://embedder.net/',
        'link4': 'https://warezcdn.com/',
    }
}

# Rota padrão '/'
@app.route('/')
def home():
    return render_template('index.html', dados=dados)

# Rota '/api' para retornar os dados em formato JSON
@app.route('/api')
def api():
    return jsonify(dados)

# Redireciona todas as outras rotas para '/'
@app.errorhandler(404)
def page_not_found(error):
    return redirect('/')
