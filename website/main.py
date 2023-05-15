from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
db = sqlite3.connect("users.db", check_same_thread=False)
cursor = db.cursor()
# cursor.execute("create table if not exists customers ("
#                 "id integer primary key, "
#                 "name varchar(250),"
#                 " email varchar(250),"
#                 " phone_num varchar(250),"
#                 " message varchar(250))")
#

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            message = request.form.get('message')
            # print(name)
            # print(email)
            # print(phone)
            # print(message)
            with sqlite3.connect("users.db") as db:
                cursor = db.cursor()
                cursor.execute("insert into customers(name, email, phone_num, message)"
                               " values (?,?,?,?)", (name, email, phone, message))
                db.commit()
                msg = "Record successfully added"
        except:
            db.rollback()
            msg = "error in insert operation"
        finally:
            db.close()
            pass
    return render_template("contact.html")


@app.route('/post')
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
