from flask import Flask
from flask import render_template

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/registration')
def registration():
	return render_template('registration.html')

@app.route('/auth')
def auth():
	return render_template('auth.html')

@app.route('/start')
def start():
	return render_template('start.html')

if __name__ == '__main__':
	app.run(debug=True)