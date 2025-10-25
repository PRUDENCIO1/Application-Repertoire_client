from flask import Flask, render_template, request, redirect, url_for
from models import db, Client

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clients.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    clients = Client.query.all()
    return render_template("index.html", clients=clients)

@app.route("/add", methods=["GET", "POST"])
def add_client():
    if request.method == "POST":
        new_client = Client(
            nom=request.form["nom"],
            prenom=request.form["prenom"],
            telephone=request.form["telephone"],
            email=request.form["email"],
            pays=request.form["pays"]
        )
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_client.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_client(id):
    client = Client.query.get_or_404(id)
    if request.method == "POST":
        client.nom = request.form["nom"]
        client.prenom = request.form["prenom"]
        client.telephone = request.form["telephone"]
        client.email = request.form["email"]
        client.pays = request.form["pays"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit_client.html", client=client)

@app.route("/delete/<int:id>")
def delete_client(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
