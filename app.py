from flask import Flask
from models import db
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

# Create a Flask application instance
app = Flask(__name__)
CORS(app)

# setup DB resources
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///schools.db"
app.config["SQLALCHEMY_TRACKMODIFICATIONS"] = False # put a pin on this
db.init_app(app) # initialize sqlalchemy with your flask app
migrate = Migrate(app, db)

app.config["JWT_SECRET_KEY"] = "bsdtrndxfbgcnhgcf nhdg nxdfgb bgsrdfv cdv" # Change this!
app.config["JWT_AACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)
jwt = JWTManager(app)
jwt.init_app(app)


from views import *

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(enrollment_bp)
app.register_blueprint(course_bp)


# with app.app_context():
#     db.create_all() # create all non-existent tables

# RANDOM_USER_API = "https://randomuser.me/api/"










# configure how the app is run
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)