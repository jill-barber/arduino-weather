from flask import Flask, render_template
import main

app = Flask(__name__)



@app.route('/')
def hello():
    return render_template("index.html", temprature=main.temprature(), humidity=main.humidity())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


# if __name__ == "__main__":
#     app.run()