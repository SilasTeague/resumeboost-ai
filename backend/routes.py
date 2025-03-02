from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import app, db
from backend.models import User, bcrypt

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Resume Keyword Optimizer API is running!"})

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    new_user = User(
        username=data["username"],
        password=hashed_password,
        security_question=data["security_question"],
        security_answer=data["security_answer"]
    )
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.username)
        return jsonify({'access_token': 'access_token'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
    
@app.route('/optimizer', methods=['GET'])
@jwt_required()
def optimizer():
    return "TODO: Implement optimizer GUI"
    
@app.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if user and user.security_question == data['security_question']:
        user.set_password(data['new_password'])
        db.session.commit()
        return jsonify({'message': 'Password reset successful'}), 200
    else:
        return jsonify({'message': 'Invalid security answer'}), 400