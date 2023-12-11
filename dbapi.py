from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Smile@15302'
app.config['MYSQL_DB'] = 'danyal'

 
@app.route('/', methods = [ "Get", "POST"])
def index():
    if request.method == "POST":
        id = request.form['studentid']
        name = request.form['name']
        email = request.form['email']
        cityid = request.form['cityid']



        cur = mysql.connection.cursor()
        
        cur.execute("INSERT INTO persons (id, fname, email, city_id) VALUE(%s, %s, %s, %s)",(id, name, email, cityid) )
        mysql.connection.commit()
        cur.close()
        return "Successfully updated record in database"
    return render_template("index.html")





if __name__  == '__main__':
    app.run(debug=True)