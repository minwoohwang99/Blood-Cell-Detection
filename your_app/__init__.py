from flask import Flask

app = Flask(__name__)

# Import your routes
from your_app import routes

if __name__ == '__main__':
    app.run(debug=True)