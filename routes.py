# import the app variable containing the flask instance, from the app package.
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm

# these routes are mapped to view functions which tell flask what logic to run when a route is accessed
def init_routes(app):
    @app.route('/', methods = ['GET', 'POST'])
    def home():
        # if current_user.is_authenticated:
        #     return redirect('/user_profile')
        return redirect(url_for('login'))

    @app.route('/login', methods = ['GET', 'POST'])
    def login():
        form = LoginForm()
        # if post request, bind posted form data to form object and validate the form
        if form.validate_on_submit():
            return redirect(url_for('user_profile'))
            # write logic here to authenticate the user, redirect to user profile if successful
        elif form.is_submitted():
            # if the form has been submitted but the login was unsuccesful, flash an error message
            flash('Invalid Username or Password. Please try again.')
        # if get request, render the login form with no pre existing data
        return render_template('login.html', form=form)

    # add @login_required route to ensure user is authenticated before allowing access
    @app.route('/user_profile')
    def user_profile():
        user = {'username': 'Miguel'}
        posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
        ]
        return render_template('user_profile.html', user=user, posts=posts)
