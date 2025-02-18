from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

preguntas = []

@app.route('/')
def index():
    return render_template('index.html', preguntas=preguntas)

@app.route('/preguntar', methods=['POST'])
def preguntar():
    pregunta = request.form.get('pregunta')
    if pregunta:
        preguntas.append(pregunta)
    return render_template('index.html', preguntas=preguntas)

if __name__ == '__main__':
    app.run(debug=True)