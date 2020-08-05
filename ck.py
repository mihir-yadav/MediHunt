import flask
from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def index():
	return flask.render_template('index.html')

@app.route('/handle_data',methods = ['POST'])
def handle_data():
	projectpath = request.form['projectpath']
	print( projectpath)


    # return 'Hello World!'
if __name__ == '__main__':
	app.debug=True
	app.run()    