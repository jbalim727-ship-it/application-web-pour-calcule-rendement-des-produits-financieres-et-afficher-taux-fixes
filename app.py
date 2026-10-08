import json

from flask import Flask, render_template, request
from db import get_db_connection
from finance import calcul_rendement


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    produits = conn.execute('SELECT * FROM produits').fetchall()
    conn.close()

    return render_template('index.html', produits=produits)


@app.route('/calcul/<int:produit_id>', methods=['GET', 'POST'])
def calcul(produit_id):
    conn = get_db_connection()
    produit = conn.execute('SELECT * FROM produits WHERE id = ?', (produit_id,)).fetchone()
    tous_produits = conn.execute('SELECT duree, taux FROM produits ORDER BY duree').fetchall()
    conn.close()

    courbe_taux = [{'duree': p['duree'], 'taux': p['taux']} for p in tous_produits]

    resultat = None
    taux_utilise = produit['taux']
    if request.method == 'POST':
        montant = float(request.form['montant'])
        taux_utilise = float(request.form['taux'])
        duree = float(request.form['duree'])
        resultat = calcul_rendement(montant, taux_utilise, duree)

    return render_template(
        'calcul.html',
        produit=produit,
        resultat=resultat,
        taux_utilise=taux_utilise,
        courbe_taux_json=json.dumps(courbe_taux),
    )


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message_envoye = False
    if request.method == 'POST':
        nom = request.form['nom']
        message = request.form['message']
        print(f"nouveau message de {nom} : {message }")
        message_envoye = True
    return render_template('contact.html', message_envoye=message_envoye)


if __name__ == '__main__':
    app.run(debug=True)
