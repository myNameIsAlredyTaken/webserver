from flask import Flask, request
import mysql.connector

app = Flask(__name__)


def get_db():
    return mysql.connector.connect(
        host="DB_SERVER_IP",
        user="admin",
        password="DB_PASSWORD",
        database="your_db"
    )


@app.route("/", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        db = get_db()
        cur = db.cursor()
        query = f"SELECT * FROM users WHERE username='{u}' AND password='{p}'"
        cur.execute(query)
        row = cur.fetchone()
        db.close()
        if row:
            msg = f"Welcome {u}"
        else:
            msg = f"Login failed for: {u}"
    return f'''
    <form method="post">
        Username: <input name="username"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit">
    </form>
    <p>{msg}</p>
    '''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
