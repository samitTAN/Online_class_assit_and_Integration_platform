from flask_login import LoginManager

from flask import render_template, redirect, request, url_for, flash, abort

from flask_login import login_user, logout_user, login_required

from ocpweb import app, db
from ocpweb.userdata.models import User
from ocpweb.userdata.forms import LoginForm,RegistrationForm


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("您已經成功的登入系統")
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')
            return redirect(next)
    return render_template('login.html',form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("已登出")
    return redirect(url_for('home'))

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
        username=form.username.data, password=form.password.data,gender=form.gender.data)
        
        # add to db table
        db.session.add(user)
        db.session.commit()
        flash("感謝註冊本系統成為會員")
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

if __name__ == "__main__":
    app.run(debug=True)
