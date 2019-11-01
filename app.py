import requests
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/restaurants')
def listarrestaurants():
    lista = requests.get("www.foodex.com/api/restaurantes")
    lista = list(lista.values())
    return render_template('listarrestaurantes.html', lista=lista)


@app.route('/restaurants/<restaurantid>')
def verrestaurant(restaurantid):
    return render_template('verrestaurante.html')


@app.route('/restaurants/<restaurantid>/menu')
def vermenu(restaurantid):
    menu = requests.get(f'www.foodex.com/api/restaurantes/{restaurantid}/menu')
    return render_template('vermenu.html', menu=menu)


@app.route('/restaurants/<restaurantid>/reserva')
def reservar(restaurantid):
    return render_template('reservar.html')
