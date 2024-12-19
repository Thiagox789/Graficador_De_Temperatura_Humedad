from flask import Flask
from config import config
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(registro.html)

if __name__ == '__main__':
    app.config.from_object(config['desarrollador']) 
    app.run()

