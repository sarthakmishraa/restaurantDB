from flask import Flask, render_template, request, redirect, url_for
import psycopg2
  
app = Flask(__name__)
  
# Connect to the database
conn = psycopg2.connect(database="restaurant", user="postgres",
                        password="your password here", host="localhost", port="5432")
  
# create a cursor
cur = conn.cursor()
  
# commit the changes
conn.commit()
  
# close the cursor and connection
cur.close()
conn.close()
  
  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/res', endpoint='res')
def res():
    # Connect to the database
    conn = psycopg2.connect(database="restaurant", user="postgres",
     password="your password here", host="localhost", port="5432")
  
    # create a cursor
    cur = conn.cursor()
  
    # Select all products from the table
    cur.execute('''SELECT * FROM restaurants''')
    restaurants_data = cur.fetchall()
  
    # close the cursor and connection
    cur.close()
    conn.close()
  
    return render_template('res.html', restaurants_data=restaurants_data)

@app.route('/res_info', endpoint='res_info')
def res_info():
    # Connect to the database
    conn = psycopg2.connect(database="restaurant", user="postgres",
     password="your password here", host="localhost", port="5432")
  
    # create a cursor
    cur = conn.cursor()
  
    # Select all products from the table
    cur.execute('''SELECT * FROM restaurant_info''')
    restaurant_info_data = cur.fetchall()
  
    # close the cursor and connection
    cur.close()
    conn.close()
  
    return render_template('res_info.html', restaurant_info_data=restaurant_info_data)

@app.route('/owner', endpoint='owner')
def owner():
    # Connect to the database
    conn = psycopg2.connect(database="restaurant", user="postgres",
     password="your password here", host="localhost", port="5432")
  
    # create a cursor
    cur = conn.cursor()
  
    # Select all products from the table
    cur.execute('''SELECT * FROM owner''')
    owner_data = cur.fetchall()
  
    # close the cursor and connection
    cur.close()
    conn.close()
  
    return render_template('owner.html', owner_data=owner_data)

@app.route('/cuisines', endpoint='cuisines')
def cuisines():
    # Connect to the database
    conn = psycopg2.connect(database="restaurant", user="postgres",
     password="your password here", host="localhost", port="5432")
  
    # create a cursor
    cur = conn.cursor()
  
    # Select all products from the table
    cur.execute('''SELECT * FROM cuisines''')
    cuisines_data = cur.fetchall()
  
    # close the cursor and connection
    cur.close()
    conn.close()
  
    return render_template('cuisines.html', cuisines_data=cuisines_data)

@app.route('/menu_items', endpoint='menu_items')
def menu_items():
    # Connect to the database
    conn = psycopg2.connect(database="restaurant", user="postgres",
     password="your password here", host="localhost", port="5432")
  
    # create a cursor
    cur = conn.cursor()
  
    # Select all products from the table
    cur.execute('''SELECT * FROM menu_items''')
    menu_items_data = cur.fetchall()
  
    # close the cursor and connection
    cur.close()
    conn.close()
  
    return render_template('menu_items.html', menu_items_data=menu_items_data)

@app.route('/reviews', endpoint='reviews')
def reviews():
    # Connect to the database
    conn = psycopg2.connect(database="restaurant", user="postgres",
     password="your password here", host="localhost", port="5432")
  
    # create a cursor
    cur = conn.cursor()
  
    # Select all products from the table
    cur.execute('''SELECT * FROM reviews''')
    reviews_data = cur.fetchall()
  
    # close the cursor and connection
    cur.close()
    conn.close()
  
    return render_template('reviews.html', reviews_data=reviews_data) 
  
if __name__ == '__main__':
    app.run(debug=True)