from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from flask_login import login_required
from app.models import User
from app import app
from app.forms import LoginForm
from flask import request
from werkzeug.urls import url_parse
from app.forms import RegistrationForm
from app import db



@app.route('/')
@app.route('/index')
def index():
    projects = [
        {
            'name': 'B&V Volcano',
            'cost': '$ 36.30',
            'completion': '72%',
            'image': 'volcano.jpg',
            'description': 'The baking soda and vinegar volcano is a classic expirement famously known for creating a mini explosion after a chemical reaction is created between two different rectants, and it is all contained within a scaled volcano model.',
            'related_links': {'Wikipedia': 'https://en.wikipedia.org/wiki/Volcano', 'National Geographic': 'https://www.nationalgeographic.com/environment/natural-disasters/volcanoes/' },
        },
        {
            'name': 'Solar Powered Car',
            'cost': '$ 20.50',
            'completion': '28%',
            'image': 'solar-car.jpg',
            'description': 'The solared power car is a car made from materials like wood and plastic that is powered by a solar panel attached to the top. You can control it with sensors, or go the remote control option.',
            'related_links': {},

        },
        {
            'name': 'Juice Powered Battery',
            'cost': '$ 18.55',
            'completion': '97%',
            'image': 'juice-battery.jpg',
            'description': 'The juice powered battery is a renewable, and non-toxic battery that is powered with biofuel, in a non-processed form such as fruits, and specifically the juice from lemons and apples.',
            'related_links': {},
        },
        {
            'name': 'DIY Telescope',
            'cost': '$ 8.40',
            'completion': '1%',
            'image': 'Telescopes.jpg',
            'description': 'The DIY Telescope is mainly people who are crafty and into astronomy. It is a home-made telescope built from materials such as cardboard and hard plastic. It lets the user ',
            'related_links': {},
        }
    ]
    return render_template('project.html', title='Project', projects=projects)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('project'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('project')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/project')
@login_required
def project():
    projects = [
        {
            'name': 'B&V Volcano',
            'cost': '$ 36.30',
            'completion': '72%',
            'image': 'volcano.jpg',
            'description': 'The baking soda and vinegar volcano is a classic expirement famously known for creating a mini explosion after a chemical reaction is created between two different rectants, and it is all contained within a scaled volcano model.',
            'related_links': {'Wikipedia': 'https://en.wikipedia.org/wiki/Volcano', 'National Geographic': 'https://www.nationalgeographic.com/environment/natural-disasters/volcanoes/' },
        },
        {
            'name': 'Solar Powered Car',
            'cost': '$ 20.50',
            'completion': '28%',
            'image': 'solar-car.jpg',
            'description': 'The solared power car is a car made from materials like wood and plastic that is powered by a solar panel attached to the top. You can control it with sensors, or go the remote control option.',
            'related_links': {'Energy Sage': 'https://news.energysage.com/what-is-solar-energy/'},

        },
        {
            'name': 'Juice Powered Battery',
            'cost': '$ 18.55',
            'completion': '97%',
            'image': 'juice-battery.jpg',
            'description': 'The juice powered battery is a renewable, and non-toxic battery that is powered with biofuel, in a non-processed form such as fruits, and specifically the juice from lemons and apples.',
            'related_links': {},
        },
        {
            'name': 'DIY Telescope',
            'cost': '$ 8.40',
            'completion': '1%',
            'image': 'Telescopes.jpg',
            'description': 'The DIY Telescope is mainly people who are crafty and into astronomy. It is a home-made telescope built from materials such as cardboard and hard plastic. It lets the user ',
            'related_links': {},
        }
    ]
    return render_template('project.html', title='Project', projects=projects)

@app.route('/projects')
def projects():
    user = {'username': 'Kaarthi'}
    posts = [
        {
            'creator': {'username': 'James'},
            'project': 'Hello fellow CODERS, check out my new solar-powered car.'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'That is an okay project, but check out my amazing volcano!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
    