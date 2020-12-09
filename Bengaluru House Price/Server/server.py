from flask import Flask

app = Flask(__name__)
@app.route('/hello')
def hello():
    return 'HI'
if __name__ == "__main__":
    print("Starting flask server")
    app.run()
