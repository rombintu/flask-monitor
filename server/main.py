from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from requests import get
from .models import Agent
from datetime import datetime

import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'GET':
        agents = Agent.query.all()
        return render_template('profile.html', name=current_user.name, agents=agents)
    if request.method == 'POST':
        return render_template('profile.html', name=current_user.name, agents=agents)


@main.route('/agent/<id>/')
@login_required
def agents(id):
    agent = Agent.query.filter_by(id=id)
    return render_template('agent.html', agent=agent)


@main.route('/add_agent')
@login_required
def add_agent():
    return render_template('add_agent.html')

@main.route('/commit_agent', methods=['POST'])
@login_required
def commit_agent(): 
    dt = (datetime.now()).strftime("%A, %d. %B %Y %I:%M%p")
    agent = Agent(request.form['hostname'], request.form['ip'], 0, 0, 0, 0, 0, 0, dt)
    db.session.add(agent)
    db.session.commit()
    return redirect('/profile')

@main.route('/update_agent', methods=['POST'])
@login_required
def update_agent(): 
    id = request.form.get('id')
    agent = Agent.query.filter_by(id=id).first()
    ip = agent.get_ip()
    try:
        data = json.loads(get(f'http://{ip}/info.json', timeout=5).text)
        agent.cpu_min = data['cpu_min']
        agent.cpu_max = data['cpu_max']
        agent.mem_min = data['mem_min']
        agent.mem_max = data['mem_max']
        agent.hard_min = data['hard_min']
        agent.hard_max = data['hard_max']
        agent.data_fresh = (datetime.now()).strftime("%A, %d. %B %Y %I:%M%p")

        db.session.commit()
    except Exception as e:
        flash('Connection timeout')
        print(e)
    return redirect(f'/agent/{id}/')


@main.route('/delete_agent', methods=['POST'])
@login_required
def delete_agent(): 
    id = request.form.get('id')
    agent = Agent.query.filter_by(id=id).first()
    db.session.delete(agent)
    db.session.commit()
    return redirect('/profile')


@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404