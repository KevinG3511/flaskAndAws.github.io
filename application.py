from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "Esta es la api de Kevin :)"

if __name__ == "__main__":
    application.run(port= 8000,debug=True)