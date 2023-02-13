from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Este es la api de Kevin :)"

if __name__ == "__main__":
    app.run(debug=True)