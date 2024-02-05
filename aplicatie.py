from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Conectare la baza de date MongoDB Atlas
client = MongoClient("mongodb+srv://MihaiCiurea:MihaiCiureaParola@cluster0.awcgm1r.mongodb.net/DataBase?retryWrites=true&w=majority")
db = client.DataBase

# Definirea structurii colecției în baza de date
collection = db.DataBaseColection


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        # Obținerea datelor din formular
        nume = request.form['nume']
        prenume = request.form['prenume']
        adresa = request.form['adresa']
        nr_tel = request.form['nr_tel']

        # Adăugarea datelor în baza de date
        person_data = {
            'Nume': nume,
            'Prenume': prenume,
            'Adresa': adresa,
            'Nr_Tel': nr_tel
        }
        collection.insert_one(person_data)

    return redirect(url_for('index'))


@app.route('/view')
def view():
    # Obținerea tuturor datelor din baza de date
    persons = collection.find()
    return render_template('view.html', persons=persons)


if __name__ == '__main__':
    app.run(debug=True)
