from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comando', methods=['POST'])
def comando():
    botao = request.form['botao']
    print(f'Botão clicado: {botao}')
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)