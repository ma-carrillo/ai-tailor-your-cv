from flask import Flask

import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
template_path = os.path.join(root_path, 'templates')
static_path = os.path.join(root_path, 'static')

app = Flask(__name__, template_folder=template_path, static_folder=static_path)


from app import routes
