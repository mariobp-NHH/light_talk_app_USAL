from flask import render_template, Blueprint, redirect, flash, url_for
from capp.users.forms import RegistrationForm, LoginForm

users=Blueprint('users',__name__)

@users.route('/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
      flash('¡Tu cuenta ha sido creada! ¡Ahora puedes iniciar sesión!', 'success')
      return redirect(url_for('users.login'))
  return render_template('users/register.html', title='register', form=form)

@users.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('¡Has iniciado sesión! ¡Ahora puedes empezar a utilizar nuestra aplicación Light Talk!', 'success')
    return redirect(url_for('home.home_home'))
  return render_template('users/login.html', title='login', form=form)