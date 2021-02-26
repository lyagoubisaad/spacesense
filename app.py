from flask import Flask, render_template,request,json
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'etudiant'
app.config['MYSQL_DB'] = 'sense'
mysql = MySQL(app)
@app.route('/',methods=["POST","GET"])
def index():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        resultValue = cur.execute("select * from labels")
        if resultValue > 0:
            labels = cur.fetchall()
            list(labels)
            labels = json.dumps(labels)
            return render_template('index.html',labels=labels)
    elif request.method == 'POST':
        figure = request.form['figure']
        coords = request.form['coords']
        label = request.form['label']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO labels(figure,coords,label) values(%s,%s,%s)", (figure,coords,label))
        mysql.connection.commit()
        cur.close()
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)