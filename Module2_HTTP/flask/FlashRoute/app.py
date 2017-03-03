from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
   return 'hello world'
app.add_url_rule('/', 'hello', hello)

if __name__ == '__main__':
   app.run(debug = True)