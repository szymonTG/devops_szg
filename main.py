from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello world from the other side!'

@app.route('/hello/<name>')

def  hello_name(name):
	return 'Hello, %s, my dear friend!' % name



if __name__ == '__main__':
	app.run(host ='0.0.0.0', port = 5000, debug = True)


