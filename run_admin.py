from flask import Flask
from admin.views import admin

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config.from_envvar('SHOWOFF_ADMIN_CONFIG', silent=True)

app.register_blueprint(admin, url_prefix='/showoff_admin')

if __name__ == '__main__':
    app.run(host=app.config['ADMIN_HOST'], port=app.config['ADMIN_PORT'])

