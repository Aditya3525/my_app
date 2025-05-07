from flask import Flask, render_template

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Flask"},
    {"id": 2, "title": "Deploy to Render"},
]

@app.route('/')
def index():
    return render_template("index.html", tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
