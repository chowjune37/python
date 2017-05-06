from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route('/service')
def services(): 
	return render_template('index.html',title='service')

@app.route('/about')
def about(): 
	return render_template('index.html',title='about')

@app.route('/')
def hello_word(): 
	return render_template('index.html',title='nihao')

if __name__ == '__main__':
	app.run()