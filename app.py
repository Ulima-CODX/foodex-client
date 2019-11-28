from flask import Flask, render_template, request, session, redirect, url_for
import wrapper
import binascii
import os
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        request.form.get('inputEmail')
        if request.form.get('inputEmail') == 'admin@test.com' and request.form.get('inputPassword') == 'abc123':
            user = wrapper.getclienteprofile('MYyrSfD7rIfAfjpNzad2sU0mOAu2')
            session['client_id'] = 'MYyrSfD7rIfAfjpNzad2sU0mOAu2'
            session['user_name'] = user['first_name'] + ' ' + user['last_name']
            session['authenticated'] = True
            session.permanent = True
            return redirect(url_for('listarrestaurants'))
        else:
            session['authenticated'] = False
            session['client_id'] = ''
            session['user_name'] = ''
            session.permanent = False
    return render_template('login.html')


@app.route('/profile')
def verprofile():
    if not isauthenticated():
        return redirect(url_for('login'))
    establishments = {}
    auxs = wrapper.getestablishments()
    for aux in auxs:
        establishments[aux['id']] = aux['name']
    response = {'user_name': session['user_name'],
                'user': wrapper.getclienteprofile(session['client_id']),
                'reservations': wrapper.getreservationbyclient(session['client_id']),
                'establishments': establishments}
    return render_template('profile.html', response=response)


@app.route('/restaurants')
def listarrestaurants():
    if not isauthenticated():
        return redirect(url_for('login'))
    response = {'user_name': session['user_name'],
                'establishments': wrapper.getestablishments()}
    return render_template('listarrestaurantes.html', response=response)


@app.route('/restaurants/<restaurantid>')
def verrestaurant(restaurantid):
    if not isauthenticated():
        return redirect(url_for('login'))
    response = {'user_name': session['user_name'],
                'establishment': wrapper.getestablishment(restaurantid)}
    return render_template('verrestaurante.html', response=response)


@app.route('/restaurants/<restaurantid>/menu')
def vermenu(restaurantid):
    if not isauthenticated():
        return redirect(url_for('login'))
    menu = wrapper.getestablishment(restaurantid)['menu_id']
    response = {'user_name': session['user_name'],
                'dishes': wrapper.getdishesbymenu(menu)}
    return render_template('vermenu.html', response=response)


@app.route('/restaurants/<restaurantid>/reserva', methods=['GET','POST'])
def reservar(restaurantid):
    if not isauthenticated():
        return redirect(url_for('login'))
    response = {'user_name': session['user_name'],
                'establishment_id': restaurantid}
    if request.method == 'POST':
        payload = {'client_id': session['client_id'],
                   'establishment_id': restaurantid,
                   'order_ids': [],
                   'attendees': 0,
                   'comment': ""}
        try:
            payload['attendees'] = int(request.form.get('comensales'))
        except:
            payload['attendees'] = 1
        try:
            fecha = datetime.datetime.strptime(request.form.get('fecha'), '%Y-%m-%d %H:%M:%S.%f')
        except:
            fecha = datetime.datetime.now()
        payload['comment'] = request.form.get('comentario')
        if wrapper.setservation(restaurantid,payload) == {}:
            pass
        else:
            redirect(url_for('listarrestaurants',restaurantid=restaurantid))
    return render_template('reservar.html', response=response)

@app.route('/restaurants/<restaurantid>/orden')
def verorden(restaurantid):
    if not isauthenticated():
        return redirect(url_for('login'))
    response = {'user_name': session['user_name'],
                'order': None,
                'dishes': []}
    orders = wrapper.getordersbyclient(session['client_id'])
    for order in orders:
        if order['establishment_id'] == restaurantid:
            response['order'] = order
            for dish_id in order['dish_ids']:
                dish = wrapper.getdish(dish_id)
                dish_added = {}
                dish_added['name'] = dish['name']
                dish_added['description'] = dish['description']
                dish_added['price'] = float(dish['price']) * int(order['dish_ids'][dish_id])
                dish_added['quantity'] = order['dish_ids'][dish_id]
                response['dishes'].append(dish_added)
            response['quantity'] = len(response['dishes'])
            break
    return render_template('verorden.html', response=response)

def isauthenticated():
    if 'authenticated' in session:
        if session['authenticated']:
            return True
    session['user_name'] = ''
    session['user_id'] = ''
    session.permanent = False
    return False


if __name__ == '__main__':
    app.run(debug=True)
