from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/tengoi")
def tengoi():
    return render_template("tengoi.html")

@app.route("/dialy")
def dialy():
    return render_template("dialy.html")

@app.route("/lichsu")
def lichsu():
    return render_template("lichsu.html")

@app.route("/chinhtri")
def chinhtri():
    return render_template("chinhtri.html")

@app.route("/kinhte")
def kinhte():
    return render_template("kinhte.html")

@app.route("/nhankhau")
def nhankhau():
    return render_template("nhankhau.html")

@app.route("/vanhoa")
def vanhoa():
    return render_template("vanhoa.html")