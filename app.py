from flask import Flask, render_template, g
import sqlite3

DATABASE = "banco.bd"
SECRET_KEY = "chave"

app = Flask("Hello")
app.config.from_object(__name__)

def conecta_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def antes_requisicao():
    g.bd = conecta_bd()

@app.teardown_request
def depois_requisicao(e):
    g.bd.close()

@app.route("/")
def exibir_entradas():
    sql = "SELECT titulo, texto, criado_em FROM entradas ORDER BY id DESC;"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto, criado_em in cur.fetchall():
        entradas.append({"titulo": titulo, "texto": texto, "criado_em": criado_em})
    return render_template("layout.html", entradas=entradas)