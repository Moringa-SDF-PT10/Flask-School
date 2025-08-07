from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy import MetaData

db = SQLAlchemy()
metadata = MetaData()

class Student(db.Model, SerializerMixin):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(200), default=f"{id}@sample.com", nullable=False, unique=True)
    boarding_house = db.Column(db.Integer, db.ForeignKey("boarding_houses.id"), nullable=True)
    bio = db.Column(db.String, nullable=True)

    # reg_code = db.Column(db.String(200), nullable=False, unique=True)

    enrollments = db.relationship("Enrollment", back_populates='student', cascade="all, delete-orphan")

    __table_args__ = (
        db.CheckConstraint('age >= 18'),
    )


    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "full_nameXYZ": self.full_name,
    #         "age---": self.age,
    #         "*****email": self.email,
    #         "___enrollments": [e.course.dict_short() for e in self.enrollments]
    #     }
    
    def dict_short(self):
        return {
            "id": self.id,
            "name": self.full_name
        }
    

    @validates("email", "age")
    def validate_email_or_age(self, key, value):
        if key == "email" and '@' not in value:
            raise ValueError("This email is definitely not valid")
        elif key == "age" and value < 18:
            raise ValueError("You are underage") 
        return value
    
    @validates("bio")
    def validate_bio(self, key, value):
        if " AI " in value:
            return "No useful bio"
        return value


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)


    enrollments = db.relationship("Enrollment", back_populates='course', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.name,
            "students": [ e.student.to_dict() for e in self.enrollments]
        }
    
    def dict_short(self):
        return {
            "id": self.id,
            "title": self.name
        }

employee_meetings = db.Table(
    'student_course_join',
    metadata,
    db.Column('student_id', db.Integer, db.ForeignKey(
        'students.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey(
        'courses.id'), primary_key=True)
)

class Enrollment(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)

    student = db.relationship("Student", back_populates="enrollments")
    course = db.relationship("Course", back_populates="enrollments")

    def to_dict(self):
        return {
            "id": self.id,
            "course": self.course.dict_short(),
            "student": self.student.dict_short()
        }


class BoardingHouse(db.Model):
    __tablename__ = "boarding_houses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    mascot = db.Column(db.String(200), nullable=False)