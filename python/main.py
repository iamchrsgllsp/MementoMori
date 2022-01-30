from distutils.log import debug
import flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"



if __name__ == '__main__':
    app.run(debug=True)