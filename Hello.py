from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/users/<name>')
def users(name):
    return 'hi %s!' % name

@app.route('/contacts')
def contacts():
    return 'contacts'

if __name__=='__main__':
    app.run()

