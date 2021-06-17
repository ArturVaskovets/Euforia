from flask import Flask, render_template, url_for, abort, redirect, request
from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template

app = Flask(__name__)
Mobility(app)

@app.before_request
def disable_mobile_version():
    if request.MOBILE and \
            request.endpoint != "home" \
            and 'static' not in request.endpoint:
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
                "brand": "Euforia",
                "price": 60,
                "material": "Plata",
                "description": "Anillo grueso de plata decorado con piedras y una circonita",
                "pictures": [
                    {
                        "url": url_for('static', filename='img/products/1/1_amarillo.png'),
                        "color": "Amarillo"
                    },
                    {
                        "url": url_for('static', filename='img/products/1/1_azul.png'),
                        "color": "Azul"
                    },
                    {
                        "url": url_for('static', filename='img/products/1/1_turquesa.png'),
                        "color": "Turquesa"
                    }
                ]
            },
            {
                "brand": "Euforia",
                "price": 50,
                "material": "Plata",
                "description": "Anillo fino de plata, en forma de “V” con una piedra de circonita en medio",
                "pictures": [
                    {
                        "url": url_for('static', filename='img/products/2/2_amarillo.png'),
                        "color": "Amarillo"
                    },
                    {
                        "url": url_for('static', filename='img/products/2/2_azul.png'),
                        "color": "Azul"
                    },
                    {
                        "url": url_for('static', filename='img/products/2/2_turquesa.png'),
                        "color": "Turquesa"
                    }
                ]
            },
            {
                "brand": "Euforia",
                "price": 68,
                "material": "Plata",
                "description": "Anillo fino de plata con tres piedras de circonita en forma de rombo.",
                "pictures": [
                    {
                        "url": url_for('static', filename='img/products/3/3_amarillo.jpg'),
                        "color": "Amarillo"
                    },
                    {
                        "url": url_for('static', filename='img/products/3/3_azul.jpg'),
                        "color": "Azul"
                    },
                    {
                        "url": url_for('static', filename='img/products/3/3_turquesa.jpg'),
                        "color": "Turquesa"
                    }
                ]
            },
            {
                "brand": "Euforia",
                "price": 35,
                "material": "Plata",
                "description": "Anillo fino con decorado trenzado y una piedra de circonita redonda",
                "pictures": [
                    {
                        "url": url_for('static', filename='img/products/4/4_amarillo.png'),
                        "color": "Amarillo"
                    },
                    {
                        "url": url_for('static', filename='img/products/4/4_rosa.png'),
                        "color": "Rosa"
                    },
                    {
                        "url": url_for('static', filename='img/products/4/4_turquesa.png'),
                        "color": "Turquesa"
                    }
                ]
            },
            {
                "brand": "Euforia",
                "price": 75,
                "material": "Plata",
                "description": "Anillo fino de plata con decoración simétrica de dos piedras circonitas a los lados y una de tamaño mayor en medio",
                "pictures": [
                    {
                        "url": url_for('static', filename='img/products/5/5_amarillo.jpg'),
                        "color": "Amarillo"
                    },
                    {
                        "url": url_for('static', filename='img/products/5/5_turquesa.jpg'),
                        "color": "Turquesa"
                    }

                ]
            },
            {
                "brand": "Euforia",
                "price": 57,
                "material": "Plata",
                "description": "Anillo abierto con dos piedras circonitas de colores en los extremos",
                "pictures": [
                    {
                        "url": url_for('static', filename='img/products/6/6_azul.jpg'),
                        "color": "Azul"
                    },
                    {
                        "url": url_for('static', filename='img/products/6/6_morado.jpg'),
                        "color": "Morado"
                    }

                ]
            },
            {
                "brand": "Euforia",
                "price": 30,
                "material": "Plata",
                "description": "Sencillo anillo de plata, fino y liso",
                "pictures": [
                    {
                        "url": url_for('static', filename='img/products/7/7_plata.jpg')
                    }

                ]
            },
            {
                "brand": "Euforia",
                "price": 125,
                "material": "Oro",
                "description": "Anillo fino de oro decoración en forma de estrella y piedras preciosas de colores",
                "pictures": [
                    {
                        "url": url_for('static', filename='img/products/8/8_blanco.jpg'),
                        "color": "Blanco"
                    },
                    {
                        "url": url_for('static', filename='img/products/8/8_verde.jpg'),
                        "color": "Verde"
                    }

                ]
            },
            {
                "brand": "Euforia",
                "price": 200,
                "material": "Oro",
                "description": "Anillo grueso de oro con agujeros rectangulares y decoración de piedras preciosas",
                "pictures": [
                    {
                        "url": url_for('static', filename='img/products/9/9_blanco.jpg'),
                        "color": "Blanco"
                    },
                    {
                        "url": url_for('static', filename='img/products/9/9_rosa.jpg'),
                        "color": "Rosa"
                    }

                ]
            },
            {
                "brand": "Euforia",
                "price": 125,
                "material": "Oro",
                "description": "Anillo fino de oro en forma de “V” con decoración de ágata y circonitas de colores",
                "pictures": [
                    {
                        "url": url_for('static', filename='img/products/10/10_blanco.png'),
                        "color": "Blanco"
                    },
                    {
                        "url": url_for('static', filename='img/products/10/10_marron.png'),
                        "color": "Marron"
                    },
                    {
                        "url": url_for('static', filename='img/products/10/10_rosa.png'),
                        "color": "Rosa"
                    }
                ]
            },
            {
                "brand": "Euforia",
                "price": 75,
                "material": "Oro",
                "description": "Anillo fino de oro decorado con piedras circonitas de colores",
                "pictures": [
                    {
                        "url": url_for('static', filename='img/products/11/11_blanco.jpg'),
                        "color": "Blanco"
                    },
                    {
                        "url": url_for('static', filename='img/products/11/11_verde.jpg'),
                        "color": "Verde"
                    }
                ]
            }
        ]
    }

    min_price = max_price = data.get("jewelry")[0].get("price")
    for product in data.get("jewelry"):
        if product.get("price") < min_price:
            min_price = product.get("price")
        if product.get("price") > max_price:
            max_price = product.get("price")

    data["jewelry_min_price"] = min_price
    data["jewelry_max_price"] = max_price


    return render_template('shopping.html', **data)


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