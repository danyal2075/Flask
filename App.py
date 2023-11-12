from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    name = input('Please Enter Your Name')
    data1 = {'name':'Danyal',
             'aeg':29}
    
    return render_template('home.html', data = {'name':name}), jsonify(data1)




@app.route('/about', methods = ['GET', 'POST'])
def about():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
    return render_template('about.html', results = {'result':result})

if __name__ == '__main__':
    app.run(debug=True)