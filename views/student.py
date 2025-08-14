from models import db, User,  BoardingHouse
from flask import jsonify, request, jsonify, make_response, Blueprint
from werkzeug.security import generate_password_hash
user_bp = Blueprint("user_bp", __name__)

# Add student

@user_bp.route("/users", methods=["POST"])
def add_student():
    data = request.json

    full_name = data["full_name"]
    age = int( data["age"] )
    email = data.get("email")
    boarding_house = data.get("boarding_house")
    bio = data.get("bio")
    password = data.get("password")

    new_student = User(
        full_name=full_name,
        age=age,
        email=email,
        boarding_house=boarding_house,
        bio=bio,
        password=  generate_password_hash( password )
    )

    db.session.add(new_student)
    db.session.commit()

    return jsonify(new_student.to_dict()), 201


# READ all students
@user_bp.route("/users", methods=["GET"])
def get_students():
    students = User.query.all()
    students_data = [student.to_dict() for student in students ]
    return make_response(students_data, 200)
    
# fetch student by id
@user_bp.route("/user/<int:id>", methods=["GET"])
def get_student(id):
    student = User.query.get_or_404(id)
    return make_response(student.to_dict(), 200)

# UPDATE student by ID
@user_bp.route("/users/<int:id>", methods=["PUT", "PATCH"])
def edit_student(id):
    student = User.query.get_or_404(id)
    
    data = request.get_json()
    student.boarding_house = data.get("boarding_house", student.boarding_house)
    student.full_name = data.get("full_name", student.full_name)
    student.age = int( data.get("age", student.age) )
    student.bio = data.get("bio", student.bio)
    student.email = data.get("email", student.email)

    db.session.commit()
    return jsonify(student.to_dict()), 200

# DELETE student by ID
@user_bp.route("/users/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = User.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({ "success": f"Deleted student with id {id} successfully" }), 200





# READ all boarding houses
@user_bp.route("/houses", methods=["GET"])
def get_houses():
    houses = BoardingHouse.query.all()
    houses_data = [h.to_dict() for h in houses ]
    return jsonify(houses_data), 200

@user_bp.route("/houses", methods=["POST"])
def add_house():
    data = request.get_json()
    name = data["name"]
    mascot = data["mascot"]

    new_house = BoardingHouse(name=name, mascot=mascot)
    db.session.add(new_house)
    db.session.commit()

    return jsonify(new_house.to_dict()), 201



# ---------------------------Student Operations---------------------------
# Create Student with Random Details
# @user_bp.route("/users/random", methods=["POST"])
# def create_random_student():
#     response = requests.get(url=RANDOM_USER_API)
#     random_user = response.json()["results"][0]


#     name_details = random_user["name"]
#     full_name = f'{name_details["title"]}, {name_details["first"]} {name_details["last"]}'

#     dob = random_user["dob"]
#     age = dob["age"]

#     email = random_user["email"]

#     student =  Student(full_name=full_name, age=age, email=email) 
#     db.session.add(student)
#     db.session.commit()

#     return make_response(student.to_dict(), 200)
