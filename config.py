import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# TODO IMPLEMENT DATABASE URL ✅
SQLALCHEMY_DATABASE_URI = "postgres://carlbowen@localhost:5432/fyrrur"
SQLALCHEMY_TRACK_MODIFICATIONS = True