from flask import Flask, render_template, url_for, abort, redirect, request
from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template

app = Flask(__name__)
Mobility(app)

@app.before_request
def disable_mobile_version():
    print(request.endpoint)
    if request.MOBILE and \
            request.endpoint != "home" \
            and 'static' not in request.endpoint:
        print("redirected")
        return redirect(url_for("home"), 302)

@app.route('/')
@mobile_template('{mobile/}home.html')
def home(template):
    data = {
        "current_section": "home",
        "header_extra_image": url_for('static', filename='img/2021.png'),
        "full_width_blocks": [
            {
                "bg_img": url_for('static', filename='img/pandora.png'),
                "caption": "Descubre pandora",
                "extra_class": "pandora"
            },
            {
                "bg_img": url_for('static', filename='img/calvin_klein.png'),
                "caption": "Calvin Klein",
                "extra_class": "calvin_klein"
            },
            {
                "bg_img": url_for('static', filename='img/red_girl.png'),
                "caption": "Oro vivo",
                "extra_class": "red_girl"
            },
            {
                "bg_img": url_for('static', filename='img/blue_girl.png'),
                "caption_title": "Galería",
                "caption_desc": "Envíanos tu fotografía favorita <br> con nuestras joyas <br>"
                                " y cada mes publicaremos 4 mejores <br> en nuestra página web",
                "caption_link": url_for('gallery'),
                "extra_class": "blue_girl"
            }
        ]
    }
    return render_template(template, **data)

@app.route('/galeria')
def gallery():
    data = {
        "current_section": "gallery",
        "header_extra_image": url_for('static', filename='img/gallery_title.png'),
        "gallery" : [
            {
                "url": url_for('static', filename='img/gallery/img_1.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_2.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_3.jpg'),
                "width": "calc((100% - 25px) / 2)",
            },
            {
                "url": url_for('static', filename='img/gallery/img_4.jpg'),
                "width": "calc((100% - 25px) / 2)",
            },
            {
                "url": url_for('static', filename='img/gallery/img_5.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_6.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_7.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_8.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_9.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_10.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_11.jpg')
            }
        ]
    }

    return render_template('gallery.html', **data)

@app.route('/joyas')
def jewelry():
    data = {
        "current_section": "jewelry",
        "header_extra_image": url_for('static', filename='img/models.png'),
        "jewelry" : [
            {
                "url": url_for('static', filename='img/gallery/img_1.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_2.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_3.jpg'),
                "width": "calc((100% - 25px) / 2)",
            },
            {
                "url": url_for('static', filename='img/gallery/img_4.jpg'),
                "width": "calc((100% - 25px) / 2)",
            },
            {
                "url": url_for('static', filename='img/gallery/img_5.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_6.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_7.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_8.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_9.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_10.jpg')
            },
            {
                "url": url_for('static', filename='img/gallery/img_11.jpg')
            }
        ]
    }

    return render_template('gallery.html', **data)


@app.errorhandler(400)
def bad_request(error):
    return render_template("error.html", message="There are errors in request.",
                           image=url_for('static', filename='img/400.jpg')), 400

@app.errorhandler(403)
def forbidden(error):
    return render_template("error.html", message="You don't have permission to access this resource.",
                           image=url_for('static', filename='img/403.jpg')), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", message="Requested resource doesn't exist.",
                           image=url_for('static', filename='img/404.jpg')), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("error.html", message="Sorry, server can not process the request.",
                           image=url_for('static', filename='img/500.jpg')), 500