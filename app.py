from flask import Flask, request, send_from_directory, jsonify, make_response
from models import db, Course, Student, Enrollment, BoardingHouse, employee_meetings
from flask_migrate import Migrate
import requests

# Create a Flask application instance
app = Flask(__name__)

# setup DB resources
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///schools.db"
app.config["SQLALCHEMY_TRACKMODIFICATIONS"] = False # put a pin on this
db.init_app(app) # initialize sqlalchemy with your flask app
migrate = Migrate(app, db)

with app.app_context():
    db.create_all() # create all non-existent tables

RANDOM_USER_API = "https://randomuser.me/api/"

# CREATE student
@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()
    name = data["name"]
    age = data["age"]
    email = data["email"]
    bio = data["bio"]
    student = Student(full_name=name, age=age, email=email, bio=bio)
    db.session.add(student)
    db.session.commit()

    response = make_response(student.to_dict(), 201)
    response.headers["SchoolHeader"] = "FlaskSchool"

    return response


# Create Student with Random Details
@app.route("/students/random", methods=["POST"])
def create_random_student():
    response = requests.get(url=RANDOM_USER_API)
    random_user = response.json()["results"][0]


    name_details = random_user["name"]
    full_name = f'{name_details["title"]}, {name_details["first"]} {name_details["last"]}'

    dob = random_user["dob"]
    age = dob["age"]

    email = random_user["email"]

    student =  Student(full_name=full_name, age=age, email=email) 
    db.session.add(student)
    db.session.commit()

    return make_response(student.to_dict(), 200)


# @app.route("/joined", methods=["GET"])
# def get_joined():
#     employees = 
#     return make_response(students_data, 200)

# READ all students
@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    students_data = [student.to_dict() for student in students ]
    return make_response(students_data, 200)

# UPDATE student by ID
@app.route("/students/<int:id>", methods=["PUT", "PATCH"])
def edit_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    student.full_name = data.get("name", student.full_name)
    student.age = data.get("age", student.age)
    db.session.commit()
    return jsonify(student.to_dict()), 200

# DELETE student by ID
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({ "message": f"Deleted student with id {id} successfully" }), 200

# CREATE Course
@app.route("/courses", methods=["POST"])
def create_course():
    data = request.get_json()
    name = data["name"]
    price = data["price"]
    course = Course(name=name, price=price)
    db.session.add(course)
    db.session.commit()
    return jsonify(course.to_dict()), 201


# Enroll Students
@app.route("/enrollment", methods=["POST"])
def enroll_student():
    data = request.get_json()
    student_id = data["student_id"]
    course_id = data["course_id"]

    Course.query.get_or_404(course_id)
    Student.query.get_or_404(student_id)

    enrollment = Enrollment(course_id=course_id, student_id=student_id)

    db.session.add(enrollment)
    db.session.commit()
    return jsonify(enrollment.to_dict()), 201 


# READ all boarding houses
@app.route("/houses", methods=["GET"])
def get_houses():
    houses = BoardingHouse.query.all()
    houses_data = [h.to_dict() for h in houses ]
    return jsonify(houses_data), 200

# TODO: Implement all CRUD operations for Course and Enrollment models


# Added app routes
@app.route('/')
def index():
    return "<p>Hello Moringa World</p>"

# Courses Route
@app.route('/courses')
def courses():
    return "This is the courses page"

# course details
@app.route('/courses/<int:course_id>')
def course_details(course_id):
    return f"This is course id: {course_id}"

# course name
# @app.route('/courses/<course_id>')
# def course_name(course_id):
#     return f"This is course name: ==> {course_id}"

# path
@app.route('/courses/<path:course_file>')
def course_file(course_file):
    return f'<img src="{send_from_directory("/", course_file).data}">'

# query params
@app.route('/course_details')
def course_name():
    c_name = request.args.get("name")
    c_date = request.args.get("date")
    return f"This is course {c_name} created on date: ==> {c_date}"


@app.route('/about')
def about():
    return "About"

@app.route('/contact')
def contact():
    return " Contact"


# configure how the app is run
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)