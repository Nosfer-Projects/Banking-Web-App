from flask import Flask, render_template, request, redirect
from modules.customer import Customer
from modules.import_sql import Sql_import
from modules.update_sql import Sql_update

customer_data= None
BALANCE = 0


app = Flask(__name__)
app.secret_key = "pass to app"

@app.route("/")
def index():
    #Homepage
    return render_template("index.html")

@app.route("/about")
def about():
    #Section About
    return render_template("about.html")

@app.route("/log_in", methods = ['POST', 'GET'])   
def log_in():
    #Page to log in by user
    global BALANCE,customer_data
    #After entering the client's login and password, the data is downloaded for verification
    if request.method == "POST":
        customer_id= request.form["customer_id"]
        password = request.form["password"]
        try:
            #We checking for data for specific customer
            data = Sql_import()
            customer_data= data.data(customer_id)
            user_password = customer_data[2]
            #If login and password are correct we will get redirect to account view
            if user_password == password:
                BALANCE = customer_data[5]    
                return redirect("account")
        except:
            #if not we will get again blank fields in login and password, and we will not able to log in.
            return render_template("log_in.html")

    return render_template("log_in.html")


@app.route("/account", methods = ['POST', 'GET'])
def account():
    #After logging in the client, you will get a personalized interface
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
    #It will log out our user and go into homepage
    global BALANCE, customer_data
    BALANCE = 0
    customer_data = None
    return render_template("index.html")                

        
        

if __name__ == "__main__":
    app.run()
