#!/usr/bin/env python3
# =============================================================================
# Citizen Tech Shop  ::  APLICACAO INTENCIONALMENTE VULNERAVEL (apenas treino)
# Global Solution - Citizen Tech | DevSecOps
# NAO USE EM PRODUCAO. Este codigo contem falhas plantadas de proposito para
# serem DETECTADAS pelos alunos com ferramentas de SAST/segredos/SCA/DAST.
# =============================================================================
import os
import hashlib
import pickle
import sqlite3
import subprocess
import requests
from flask import Flask, request, render_template, make_response

app = Flask(__name__)

# [VULN] segredo embutido no codigo (hardcoded secret)
app.config['SECRET_KEY'] = 'citizen-tech-super-secret-key-123'
DB_PASSWORD = "SuperSecret123!"                         # [VULN] credencial hardcoded
STRIPE_API_KEY = "stripe_demo_placeholder"  # [VULN] chave de API (falsa)


@app.route('/')
def index():
    nome = request.args.get('nome', 'cidadao')
    # [VULN] XSS refletido - entrada do usuario sem sanitizacao no template (|safe)
    return render_template('index.html', nome=nome)


@app.route('/produto')
def produto():
    pid = request.args.get('id', '1')
    con = sqlite3.connect('loja.db')
    cur = con.cursor()
    # [VULN] SQL Injection - concatenacao de string na query
    query = "SELECT nome, preco FROM produtos WHERE id = '%s'" % pid
    cur.execute(query)
    linha = cur.fetchone()
    con.close()
    return str(linha)


@app.route('/login', methods=['POST'])
def login():
    senha = request.form.get('senha', '')
    # [VULN] hash fraco (MD5) para senha
    h = hashlib.md5(senha.encode()).hexdigest()
    return {'hash': h}


@app.route('/ping')
def ping():
    host = request.args.get('host', '127.0.0.1')
    # [VULN] Command Injection - entrada concatenada em comando de shell
    saida = subprocess.check_output("ping -c 1 " + host, shell=True)
    return saida


@app.route('/calc')
def calc():
    expr = request.args.get('expr', '1+1')
    # [VULN] uso de eval com entrada do usuario (RCE)
    return str(eval(expr))


@app.route('/carregar', methods=['POST'])
def carregar():
    dados = request.get_data()
    # [VULN] desserializacao insegura (pickle) de dados nao confiaveis
    obj = pickle.loads(dados)
    return str(obj)


@app.route('/proxy')
def proxy():
    url = request.args.get('url', 'http://127.0.0.1')
    # [VULN] SSRF + verificacao TLS desabilitada
    r = requests.get(url, verify=False)
    return r.text


if __name__ == '__main__':
    # [VULN] modo debug ligado e bind em 0.0.0.0
    app.run(host='0.0.0.0', port=5000, debug=True)
