from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 8070
    app.run(debug=True, host=HOST, port=PORT)


