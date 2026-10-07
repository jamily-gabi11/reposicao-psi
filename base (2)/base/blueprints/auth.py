from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome =request.form.get("nome")
        email =request.form.get("email")
        senha =request.form.get("senha")

        conexao = conectar()
        cursor = conexao.cursor()
        senha_hash = generate_password_hash(senha)

        database.criar_usuario()
        conexao.commit()
        conexao.close()
        return redirect(url_for("auth.login"))

    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        conexao = obter_conexao()
        cursor = conexao.cursor() 

        for usuario in database.usuarios:
            if usuario["nome"] == nome and usuario["senha"] == senha:
                session["usuario"] = nome
                return redirect(url_for("index"))
        return render_template("login.html", erro="Credenciais inválidas")
    return render_template("login.html")
    
        return redirect(url_for("auth.login"))
    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("index"))

  
# Complete este arquivo durante a avaliação.
#
# O Blueprint já está criado, mas nenhuma rota foi vinculada ainda.
# Implemente aqui:
#
# - a rota /registro;
# - a rota /login;
# - a rota /logout.
