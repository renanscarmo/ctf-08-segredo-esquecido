from flask import Flask

from config import CHAVE_API

app = Flask(__name__)


@app.route("/")
def home():
    return {"mensagem": "Loja online", "chave_termina_em": CHAVE_API[-9:]}


if __name__ == "__main__":
    app.run()