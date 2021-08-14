from warnings import resetwarnings
from flask import Flask, render_template, url_for, request
from tools import Tool

app = Flask(__name__)
app.config["SECRET_KEY"] = '866a09b30d75b28b28f7fcec2ea542ef'

@app.route("/", methods=["GET", "POST"])
@app.route("/encryptor", methods=["GET", "POST"])
def encryptor():
    return render_template("encryptor.html")

@app.route("/decryptor", methods=["GET", "POST"])
def decryptor():
    return render_template("decryptor.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    to_encrypt = request.form.get("string") #to encrypt
    to_decrypt = request.form.get("encrypted") #to decrypt
    if to_encrypt:
        key = int(request.form.get("key"))
        result.result = Tool(to_encrypt, key)
        return render_template("debug.html", string=result.result)
    else:
        key = 0 - int(request.form.get("nkey"))
        result.result = Tool(to_decrypt, key)
        return render_template("debug.html", encr=result.result)

if __name__ == "__main__":
    app.run()
#use infinityfree to deploy
#add some more css