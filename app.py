from flask import Flask, render_template
from ctftimebr.models.dbhelper import DbHelper

app = Flask(__name__)

@app.route('/')
def index():
    db = DbHelper('ctftimebr/sqlite.db')
    db.connect_db()
    return render_template('index.html', ctf_list = db.list_ctf_events())

if __name__ == '__main__':
    app.run(debug = True)