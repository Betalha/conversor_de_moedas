from flask import Flask, render_template, request, jsonify
from services.conversor_service import converter_moeda
from services.taxa_cambio_service import obter_taxas_cambio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter', methods=['POST'])
def converter():
    dados = request.json
    try:
        resultado = converter_moeda(
            float(dados['valor']),
            dados['moeda_origem'],
            dados['moeda_destino']
        )
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

@app.route('/moedas')
def moedas():
    try:
        taxas = obter_taxas_cambio()
        return jsonify(list(taxas.keys()))
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=1234)