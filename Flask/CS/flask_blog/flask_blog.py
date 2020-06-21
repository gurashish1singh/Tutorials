'''
Building a basic blog app using Flask
'''
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# Initializing a flask app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b4e1625f044394f9b68507161f4f5e'

posts = [
    {
        'author': 'GS',
        'title': 'Blog Post 1',
        'content': 'First post',
        'date_posted': 'June 19, 2020'
    },
    {
        'author': 'PS',
        'title': 'Blog Post 2',
        'content': 'Second post',
        'date_posted': 'June 20, 2020'
    }
]


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='Csutom About title')


@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('homepage'))

    return render_template('register.html', title='Register Today!', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == '123456':
            flash('You have been logged in !', 'success')
            return redirect(url_for('homepage'))
        else:
            flash('Login unsuccessfull. Please check username and password', 'danger')

    return render_template('login.html', title='Login to your account!', form=form)


if __name__ == "__main__":
    app.run(debug=True)
