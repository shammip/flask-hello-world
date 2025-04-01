# Lab 10 - Use Render to Host Website & Database
# Name: Shammi Pereira
# Date: April 1, 2025

import psycopg2

from flask import Flask
app = Flask(__name__)

# Greeting
@app.route('/')
def hello_world():
    return 'Hello World from Shammi in 3308'

# Testing database
@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://cspb3308data_user:cVEDPxhcrub7Rr1N4NaxpU1Vi8sl3sCy@dpg-cvm5lu9r0fns7380utf0-a/cspb3308data")
    conn.close()
    return 'Database Connection Successful'

# Creating table 
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

# Inserting data into table 
@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://cspb3308data_user:cVEDPxhcrub7Rr1N4NaxpU1Vi8sl3sCy@dpg-cvm5lu9r0fns7380utf0-a/cspb3308data")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Populated'

# Displaying table 
@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://cspb3308data_user:cVEDPxhcrub7Rr1N4NaxpU1Vi8sl3sCy@dpg-cvm5lu9r0fns7380utf0-a/cspb3308data")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.close()
    response_string = ""
    response_string += "<table>"
    for basketball_player in records:
        response_string += "<tr>"
        for data in basketball_player: 
            response_string += f"<td>{data}</td>"
        response_string += "</tr>"
    response_string += "</table>"
    return response_string
    
# Dropping table
@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://cspb3308data_user:cVEDPxhcrub7Rr1N4NaxpU1Vi8sl3sCy@dpg-cvm5lu9r0fns7380utf0-a/cspb3308data")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Dropped'