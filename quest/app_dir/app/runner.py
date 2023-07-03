from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quest")
def first_task():
    return render_template("Quest1.html")


@app.route("/68156cdd8345f86f684df8347e0e1c62")
def second_task():
    return render_template("Quest2.html")


@app.route("/eacadb2714313e46e5a01ac9d31c5a2a")
def third_task():
    return render_template("Quest3.html")


@app.route("/74990a8c9cc6815b1006c9df1a1a2707")
def fourth_task():
    return render_template("Quest4.html")


@app.route("/cf33717186cda7c3b8a7d1ec249d88e2")
def fifth_task():
    return render_template("Quest5.html")


@app.route("/ac84e19843673cddb1bdf7d0b3897172")
def final_page():
    return render_template("final.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/d959e858f0d21a052c8cb1249c348158")
def sixth_task():
    return render_template("final.html")

