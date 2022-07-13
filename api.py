from flask import Flask, render_template
from src import covid_dash, hospitals_tb

app = Flask(__name__)
@app.route("/")
def landing_page():
return render_template('index.html')
if __name__ == '__main__':
app.run(host='0.0.0.0',port=1991, debug=True)

@app.route("/dashboard")
def dashboard():
<<<<<<< HEAD
return render_template('dashboard.html')
=======
return render_template('ÑAÑAAÑÑAÑAÑAÑAÑÑA.html')
>>>>>>> branch-ticket-3-2
@app.route("/map")
def map():
return render_template('map.html')