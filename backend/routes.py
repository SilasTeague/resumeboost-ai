from flask import request, jsonify, redirect, url_for, render_template, session
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from backend.app import app, db
from backend.models import User, bcrypt

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Resume Keyword Optimizer API is running!"})

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')

    data = request.form

    if User.query.filter_by(username=data['username']).first():
        return render_template('signup.html', error="Username already exists")

    if data["password"] != data["confirm_password"]:
        return render_template('signup.html', error="Passwords do not match")

    if len(data["password"]) < 8:
        return render_template('signup.html', error="Password must be at least 8 characters long")
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    hashed_answer = bcrypt.generate_password_hash(data["security_answer"]).decode("utf-8")

    new_user = User(
        username=data["username"],
        password_hash=hashed_password,
        security_question=data["security_question"],
        security_answer=hashed_answer
    )
    
    db.session.add(new_user)
    db.session.commit()

    access_token = create_access_token(identity=new_user.username)
    session['access_token'] = access_token
    return redirect(url_for('optimize'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    data = request.form

    if not data.get('username') or not data.get('password'):
        return render_template('login.html', error="Username and password are required")

    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.username)
        session['access_token'] = access_token
        return redirect(url_for('optimizer')), 200
    else:
        return render_template('login.html', error="Invalid credentials")
    
@app.route('/optimizer', methods=['GET'])
def optimizer():
    if 'access_token' not in session:
        return redirect(url_for('login'))
    return "TODO: Implement optimizer GUI"
    
@app.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    required_fields = ['username', 'security_question', 'security_answer', 'new_password', 'confirm_password']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'error': f'{field.replace("_", " ").title()} is required'}), 400
        
    if data["new_password"] != data["confirm_password"]:
        return jsonify({'error': 'Passwords do not match'}), 400

    if len(data['new_password']) < 8:
        return jsonify({'error': 'Password must be at least 8 characters long'}), 400

    if user and bcrypt.check_password_hash(user.security_answer, data['security_answer']):
        user.set_password(data['new_password'])
        db.session.commit()
        return jsonify({'message': 'Password reset successful'}), 200
    else:
        return jsonify({'message': 'Invalid security answer'}), 400