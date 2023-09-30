from flask import Flask, render_template,flask, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

def RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(max=60)])
    pssword = PasswordField('Password', validator=[DataRequired(), length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

@app.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        Password = form.password.data
        user= User(username=username, password=password) 
        db.session.add(user)
        db.session.commit()
        flash("Registration sucessful")
        return redirect('login')
    return render_template('register.html', form=form)

if __name__=='__main__':
    app.run(debug=True)



