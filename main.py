from flask import Flask, render_template
import psycopg2


app = Flask(__name__)

pg = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password=9518,
    port=5432)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/cities')
def read_count():
    cursor = pg.cursor()
    cursor.execute("SELECT COUNT(*) FROM city WHERE countrycode = 'BRA';")
    pgCount = cursor.fetchone()[0]
    
    result = str(pgCount) + " (from postgre)"
    
    return render_template('cities.html', value=result) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

