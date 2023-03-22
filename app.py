from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__,static_folder='static')

#Отрисовка страниц по запросу
@app.route('/registration')
def registration():
	return render_template('registration.html')

@app.route('/auth')
def auth():
	return render_template('auth.html')

@app.route('/start')
def start():
	return render_template('start.html')

#Обработка форм
@app.route('/reghandler', methods=['POST'])
def regform_handler():
	if request.method == 'POST':
		

if __name__ == '__main__':
	app.run(debug=True)