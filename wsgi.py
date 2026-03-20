import sys
import os

# Adjust this path if your username or project folder changes on the server.
# For PythonAnywhere, it will look like '/home/yourusername/final'
project_home = os.path.dirname(os.path.abspath(__file__))
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Import the Flask app factory
from app import create_app

# The WSGI server expects an object named 'application'
application = create_app()
