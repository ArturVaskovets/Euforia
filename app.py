from flask import Flask, render_template, url_for, request # pylint: disable=import-error
from flask_mobility import Mobility # pylint: disable=import-error
from flask_mobility.decorators import mobile_template # pylint: disable=import-error
app = Flask(__name__)
Mobility(app)

@app.route('/')
@mobile_template('{mobile/}home.html')
def home(template):
    data = {
        "current_section": "home",
        "header_extra_image": url_for('static', filename='img/2021.png')
    }
    return render_template(template, **data)



@app.errorhandler(400)
def bad_request(error):
	return render_template("error.html",message="There are errors in request.", image=url_for('static', filename='img/400.jpg')), 400

@app.errorhandler(403)
def forbidden(error):
	return render_template("error.html",message="You don't have permission to access this resource.", image=url_for('static', filename='img/403.jpg')),  403

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",message="Requested resource doesn't exist.", image=url_for('static', filename='img/404.jpg')),  404

@app.errorhandler(500)
def internal_server_error(error):
	return render_template("error.html",message="Sorry, server can not process the request.", image=url_for('static', filename='img/500.jpg')),  500
