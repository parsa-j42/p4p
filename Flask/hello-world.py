from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
   return 'Hello World'
@app.route('/hello/<name>')
def helllo_world(name):
   return 'Hello World %f' % name
@app.route('/page2')
def page2():
   return "hi"
if __name__ == '__main__':
   app.run(host="0.0.0.0")