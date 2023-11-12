from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    name = input('Please Enter Your Name')
    
    return render_template('home.html', data = {'name':name})

@app.route('/About')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)