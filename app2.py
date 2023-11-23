from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

data = []

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        roll = request.form['rollnumber']
        course = request.form['course']

        record1 = {'name':name,'email':email,'rollnumber':roll,'Course':course} 
        data.append(record1)

        # return render_template('home1.html', data = 'Successfully Added Data')
    return render_template('home1.html', message = 'Success')

  


        

@app.route('/about', methods =['GET','POST'])
def about():
    return render_template('about1.html', data = data)


if __name__ == '__main__':
    app.run(debug=True)