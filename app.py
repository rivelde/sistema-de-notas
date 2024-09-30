from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Carrega o CSV com as notas
df = pd.read_csv('notas.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultar-nota', methods=['POST'])
def consultar_nota():
    data = request.get_json()
    matricula = data['matricula']
    
    # Busca a nota correspondente à matrícula
    aluno = df[df['matricula'] == int(matricula)]
    if not aluno.empty:
        nota = aluno['nota'].values[0]
        return jsonify({'nota': nota})
    else:
        return jsonify({'nota': None})

if __name__ == '__main__':
    app.run(debug=True)
