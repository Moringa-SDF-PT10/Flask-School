
from models import db, Course
from flask import jsonify, request, jsonify, Blueprint

course_bp = Blueprint("course_bp", __name__)


# CREATE Course
@course_bp.route("/courses", methods=["POST"])
def create_course():
    data = request.get_json()
    name = data["name"]
    price = data["price"]

    course = Course(name=name, price=price)
    db.session.add(course)
    db.session.commit()
    return jsonify(course.to_dict()), 201

# Fetch all courses
@course_bp.route("/courses", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify([c.to_dict() for c in courses]), 200

# Fetch course by ID
@course_bp.route("/courses/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course.to_dict()), 200

# Update Course by ID
@course_bp.route("/courses/<int:id>", methods=["PUT", "PATCH"])
def update_course(id):
    course = Course.query.get_or_404(id)
    data = request.get_json()
    course.name = data.get("name", course.name)
    course.price = data.get("price", course.price)
    db.session.commit()
    return jsonify(course.to_dict()), 200

# Delete Course by ID
@course_bp.route("/courses/<int:id>", methods=["DELETE"])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({"success": f"Course {id} deleted"}), 200
