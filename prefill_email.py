from app import app
from models import db, Student

with app.app_context():
    students =  Student.query.filter(Student.email == None).all()
    for s in students:
        # Logic here
        # load file, check each id, the corresponding email, attach to that student
        s.email = f"{s.full_name}@sample.com"
    db.session.commit()