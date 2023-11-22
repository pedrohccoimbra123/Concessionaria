from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Carro:
    contador_carros = 0

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        Carro.contador_carros += 1

    def obter_informacoes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

concessionaria = []

@app.route('/')
def index():
    return 'Bem-vindo à Concessionária de Carros!'

@app.route('/carros')
def listar_carros():
    return render_template('Estoque.html', carros=concessionaria)

@app.route('/cadastro', methods=['GET', 'POST'])
def criar_carro():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        ano = request.form['ano']

        novo_carro = Carro(marca, modelo, ano)
        concessionaria.append(novo_carro)

        return redirect(url_for('listar_carros'))

    return render_template('Cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)
