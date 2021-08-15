from flask import Flask,render_template,request,flash
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Rota inicial,para carregar o template html
@app.route('/')
def indexMeme():
    return render_template('index.html',url="",info="")

# Rota com o POST
@app.route('/meme',methods=['POST'])
def meme():
    url = 'https://meme-api.herokuapp.com/gimme'
    response = requests.get(url)
    dados = response.json()
    urlMeme = dados['url']
    return render_template('index.html',url=urlMeme,info="")

# Rota com o GET
@app.route('/GOT',methods=['GET'])
def GOT():
    category = request.args.get('category')
    nome = request.args.get('nome')
    url = f'https://anapioficeandfire.com/api/{category}?name={nome}'
    response = requests.get(url)
    dados = response.json()
    if dados == []:
        flash("Nenhum dado encotrado, tente novamente !!!")
        return render_template('index.html',url="",info="")

    return render_template('index.html',url="",info=dados[0]) 
    


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True,port=67)