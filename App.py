from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Python with Flask'

@app.route('/About')
def about():
    return('<h>This is my about section</h>')

if __name__ == '__main__':
    app.run(debug=True)