from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def process_login():
    login = request.form['login']
    password = request.form['password']
    return f"Логин: {login}, Пароль: {password}"

if __name__ == '__main__':
    app.run(debug=True)
