from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(200), default=f"{id}@sample.com", nullable=False, unique=True)
    reg_code = db.Column(db.String(200), nullable=False, unique=True)

    enrollments = db.relationship("Enrollment", back_populates='student', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "age": self.age,
            "email": self.email,
            "enrollments": [e.course.dict_short() for e in self.enrollments]
        }
    
    def dict_short(self):
        return {
            "id": self.id,
            "name": self.full_name
        }
    



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