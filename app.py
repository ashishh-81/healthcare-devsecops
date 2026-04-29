from flask import Flask, render_template
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


# Home Route
@app.route('/')
def home():
    return render_template("index.html")


# Run App
if __name__ == '__main__':
    app.run(debug=True)