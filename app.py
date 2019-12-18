from flask import Flask , jsonify,render_template
from requests import get, post
import json


app = Flask(__name__)

@app.route("/accueil",methods=["GET"])
def home():
    res = get('http://localhost:9200/_aliases')
    index = res.json()

    data = get('http://localhost:9200/hobbies/_search?size=80')
    data = data.json()

    return render_template('index.html',data = data['hits']['hits'],index=index,titre="Groupe 14 : (Hobbie)")


@app.route("/", methods = ["GET"])
def get_home_page():
    return render_template("accueil.html")



@app.route("/tiger_bank_database",methods=["GET"])
def fect_my_data():
    res = get('http://localhost:9200/bank/_search')
    data = res.json()
    return jsonify(data)

@app.route("/hobbies",methods=["GET"])
def fect_my_hobbies():
    res = get('http://localhost:9200/hobbies/_search?size=80')
    data = res.json()
    return jsonify(data)

@app.route("/database_list", methods = ['GET'])
def list_databse():
    return render_template("list_database.html")

# Cette application affiche la base de données banque
@app.route("/database_bank", methods=["GET"])
def view_bank_database():
    res = get("http://localhost:9200/bank/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("database_bank.html", database=database)

@app.route("/database_groupe_1", methods=["GET"])
def view_groupe_1_database():
    res = get("http://localhost:9200/group_1/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_1.html", database=database,titre="Groupe 1 : (Cars et Camions)")

@app.route("/database_groupe_2", methods=["GET"])
def view_groupe_2_database():
    res = get("http://localhost:9200/group_2/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_2.html", database=database,titre="Groupe 2 (Offres d'emploi)")

@app.route("/database_groupe_4", methods=["GET"])
def view_groupe_4_database():
    res = get("http://localhost:9200/group_4/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_4.html", database=database,titre="Groupe 4 (Offres de services)")

@app.route("/database_groupe_3", methods=["GET"])
def view_groupe_3_database():
    res = get("http://localhost:9200/group_3/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_3.html", database=database,titre="Groupe 3 (Vehicules)")

@app.route("/database_groupe_5", methods=["GET"])
def view_groupe_5_database():
    res = get("http://localhost:9200/group_5/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_5.html", database=database,titre="Groupe 5 (Agro alimentaire)")

@app.route("/database_groupe_6", methods=["GET"])
def view_groupe_6_database():
    res = get("http://localhost:9200/group_6/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_6.html", database=database,titre="Groupe 6 (Electro-manager)  ")


@app.route("/database_groupe_7", methods=["GET"])
def view_groupe_7_database():
    res = get("http://localhost:9200/group_7/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_7.html", database=database,titre="Groupe 7 (Mode beaute)")

@app.route("/database_groupe_10", methods=["GET"])
def view_groupe_10_database():
    res = get("http://localhost:9200/group_10/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_10.html", database=database, titre="Groupe 10 (Equipement maison)")


@app.route("/database_groupe_11", methods=["GET"])
def view_groupe_11_database():
    res = get("http://localhost:9200/group_11/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_11.html", database=database,titre = "Groupe 11 (Animaux)")

@app.route("/database_groupe_12", methods=["GET"])
def view_groupe_12_database():
    res = get("http://localhost:9200/group_12/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_12.html", database=database,titre="Groupe 12 (Elevage) ")

@app.route("/database_groupe_13", methods=["GET"])
def view_groupe_13_database():
    res = get("http://localhost:9200/group_13/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_13.html", database=database,titre="Groupe 13 (Electroniques)")

@app.route("/database_groupe_8", methods=["GET"])
def view_groupe_8_database():
    res = get("http://localhost:9200/group_8/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_8.html", database=database,titre="Groupe 8 (Materiaux outils equipements)")

@app.route("/database_groupe_9", methods=["GET"])
def view_groupe_9_database():
    res = get("http://localhost:9200/group_9/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_9.html", database=database,titre="Groupe 9 (Accessoire) ")

@app.route("/database_groupe_15", methods=["GET"])
def view_groupe_15_database():
    res = get("http://localhost:9200/group_15/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("groupe_15.html", database=database,titre="Groupe 15 (Loisirs sport)")


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='localhost', port=9874)

