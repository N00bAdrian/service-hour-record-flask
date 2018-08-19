from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '6fe42bae9a1e14181d1fcf11ba912177'

from servicehour import routes
