from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import sqlite3 as sqlt


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
def regformhandler():
	if request.method == 'POST':

		email = request.form['email']
		login = request.form['login']
		password = request.form['password']


		con = sqlt.connect('./DataBase/Users.db')
		cur = con.cursor()

		#Список всех логинов в БД
		dbLogins = cur.execute("SELECT login FROM users").fetchall()
		dbLogins = [i for i, in dbLogins]

		if login in dbLogins:
			return 'Логин занят'	
		else:
			cur.execute(f"INSERT INTO users(email, login,password) VALUES('{email}', '{login}', '{password}')")
			con.commit()
			return redirect('/auth')

		cur.close()
		con.close()

@app.route('/authandler', methods=['POST'])
def authhandler():
	if request.method == 'POST':

		login = request.form['login']
		password = request.form['password']

		con = sqlt.connect('./DataBase/Users.db')
		cur = con.cursor()

		all_records = cur.execute("SELECT * FROM users").fetchall()

		#Совпадение в БД обнаружено
		match = False

		for i in range(0, len(all_records)):
			if (all_records[i][2] == login) and (all_records[i][3] == password):
				match = True

		if match:
			return 'Перенаправить на страницу опроса'
		else:
			return 'Неправильные данные'

		con.commit()
		cur.close()
		con.close()

	return f'{login} {password}'


if __name__ == '__main__':
	app.run(debug=True)