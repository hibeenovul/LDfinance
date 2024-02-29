from flask import Flask, render_template, url_for, redirect
from forms import Registrationform, Loginform
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b409f3d6a632f93c0c1c6c99217ff1ff'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.app_context().push()

# this is the class model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    

# these are the routes for the site
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/products")
def products():
    return render_template('products.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

# these is the flask registration form authentication
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registrationform()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data, email=form.email.data, phone=form.phone.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
        # return '<h1> new user has been created </h1>'
    return render_template('register.html', form=form)

# these is the flask login form authentication
@app.route("/login", methods=['GET', 'POST'])
def login():
    form =  Loginform()
    if form.validate_on_submit():
        user = User.query.filter(text("email = :email")).params(email=form.email.data).first()        
        if user:
            if user.password == form.password.data:
                return redirect(url_for('dashboard'))
            else:
                return '<h1> incorrect password, please try again! </h1>'
        else:
            return '<h1> this user does not exist </h1>'
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)