from models import db, Course, User, Enrollment
from flask import jsonify, request, jsonify, make_response, Blueprint

enrollment_bp = Blueprint("enrollment_bp", __name__)



# ---------------------------Enrollment operations---------------------------
# Enroll Students
@enrollment_bp.route("/enrollment", methods=["POST"])
def enroll_student():
    data = request.get_json()
    student_id = data["student_id"]
    course_id = data["course_id"]

    Course.query.get_or_404(course_id)
    User.query.get_or_404(student_id)

    enrollment = Enrollment(course_id=course_id, student_id=student_id)

    db.session.add(enrollment)
    db.session.commit()
    return jsonify(enrollment.to_dict()), 201 

# Fetch all enrollments
@enrollment_bp.route("/enrollments", methods=["GET"])
def get_enrollments():
    enrollments = Enrollment.query.all()
    return jsonify([e.to_dict() for e in enrollments]), 200

# Fetch enrollment by ID
@enrollment_bp.route("/enrollments/<int:id>", methods=["GET"])
def get_enrollment(id):
    enrollment = Enrollment.query.get_or_404(id)
    return jsonify(enrollment.to_dict()), 200

# Update enrollment
@enrollment_bp.route("/enrollments/<int:id>", methods=["PUT", "PATCH"])
def update_enrollment(id):
    enrollment = Enrollment.query.get_or_404(id)
    data = request.get_json()
    if "course_id" in data:
        Course.query.get_or_404(data["course_id"])
        enrollment.course_id = data["course_id"]
    if "student_id" in data:
        User.query.get_or_404(data["student_id"])
        enrollment.student_id = data["student_id"]
    db.session.commit()
    return jsonify(enrollment.to_dict()), 200

# Delete enrollment 
@enrollment_bp.route("/enrollments/<int:id>", methods=["DELETE"])
def delete_enrollment(id):
    enrollment = Enrollment.query.get_or_404(id)
    db.session.delete(enrollment)
    db.session.commit()
    return jsonify({"message": f"Enrollment {id} deleted"}), 200

