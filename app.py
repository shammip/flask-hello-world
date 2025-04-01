import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Shammi in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://cspb3308data_user:cVEDPxhcrub7Rr1N4NaxpU1Vi8sl3sCy@dpg-cvm5lu9r0fns7380utf0-a/cspb3308data")
    conn.close()
    return 'Database Connection Successful'

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://cspb3308data_user:cVEDPxhcrub7Rr1N4NaxpU1Vi8sl3sCy@dpg-cvm5lu9r0fns7380utf0-a/cspb3308data")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Created'
