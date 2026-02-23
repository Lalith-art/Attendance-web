from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Attendance Website Working!"

@app.route("/templates/calender.html")
def calender():
    return "Calender is opening"

if __name__ == "__main__":
    app.run(debug=True)
