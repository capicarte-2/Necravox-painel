from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>🚀 Painel do Necravox</h1><p>Bot online e funcionando!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)