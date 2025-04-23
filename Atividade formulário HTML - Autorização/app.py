from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

# Usuários de exemplo com roles e atributos
USERS = {
    "admin@example.com": {
        "role": "admin",
        "department": "TI"
    },
    "user@example.com": {
        "role": "user",
        "department": "Vendas"
    }
}

# Validações do lado do servidor
def validar_dados(nome, email, senha):
    if len(nome) < 3:
        return "Nome muito curto."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "E-mail inválido."
    if not re.match(r"^(?=.*[A-Z])(?=.*\d).{8,}$", senha):
        return "Senha fraca."
    return None

# RBAC: Role-Based Access Control
def rbac_autorizado(role_requerido, email):
    user = USERS.get(email)
    return user and user["role"] == role_requerido

# ABAC: Attribute-Based Access Control
def abac_autorizado(email, departamento_requerido):
    user = USERS.get(email)
    return user and user["department"] == departamento_requerido

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    erro = validar_dados(nome, email, senha)
    if erro:
        return erro, 400

    # Autorização RBAC e ABAC
    if not rbac_autorizado("admin", email):
        return "Acesso negado: precisa ser admin (RBAC)", 403

    if not abac_autorizado(email, "TI"):
        return "Acesso negado: departamento errado (ABAC)", 403

    return f"Usuário {nome} registrado com sucesso!", 200

if __name__ == '__main__':
    app.run(debug=True)