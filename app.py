from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/restaurants')
def listarrestaurants():
    return render_template('listarrestaurantes.html')


@app.route('/restaurants/<restaurantid>')
def verrestaurant(restaurantid):
    return render_template('verrestaurante.html')


@app.route('/restaurants/<restaurantid>/menu')
def vermenu(restaurantid):
    return render_template('vermenu.html')


@app.route('/restaurants/<restaurantid>/reserva')
def reservar(restaurantid):
    return render_template('reservar.html')
