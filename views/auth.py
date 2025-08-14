from models import db, User,  BoardingHouse
from flask import jsonify, request, jsonify, make_response, Blueprint
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth_bp", __name__)


# login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    password =  data["password"] 
    email = data.get("email")
    
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    
    else:
        return jsonify({"error": "Wrong credentials"})
   


