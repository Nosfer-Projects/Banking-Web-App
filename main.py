from flask import Flask, render_template, request, redirect
import psycopg2 as pg2
from customer import Customer
from import_sql import Sql_import
from update_sql import Sql_update

customer_data= None
BALANCE = 0


app = Flask(__name__)
app.secret_key = "password to app"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/log_in", methods = ['POST', 'GET'])   
def log_in():
    global BALANCE,customer_data

    if request.method == "POST":
        customer_id= request.form["customer_id"]
        password = request.form["password"]
        try:
            data = Sql_import()
            customer_data= data.data(customer_id)
            print(customer_data)
            user_password = customer_data[2]
            print(user_password)
            print(password)

            if user_password == password:
                BALANCE = customer_data[5]    
                return redirect("account")
        except:
            return render_template("log_in.html")

    return render_template("log_in.html")


@app.route("/account", methods = ['POST', 'GET'])
def account():
        global BALANCE
        error = None
        customer = Customer(customer_data)
        if request.method == "POST":
            amount = request.form["amount-text"]
            if BALANCE - int(amount) < 0:
                error = f"Transaction rejected"            
            else:
                error = 'Money transferred'
                BALANCE -= int(amount)
                update = Sql_update()
                update.update(customer.customer_id, BALANCE)


        return render_template("account.html", name=customer.name, surname=customer.surname, balance=BALANCE, error=error)
                
@app.route('/logout')
def logout():
    global BALANCE, customer_data
    BALANCE = 0
    customer_data = None
    return render_template("index.html")                

        
        

if __name__ == "__main__":
    app.run(debug=True)