from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/login')
def auth():
	return render_template('index.html')
