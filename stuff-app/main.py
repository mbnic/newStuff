# main.py

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/process', methods=['POST'])
def process():
	
	email = request.form['email']
	name = request.form['name']

	if name and email:
		return jsonify({'success' : 'Sumbitted Successfully'})

	return jsonify({'error' : 'Missing Data'})


if __name__ == "__main__":
	app.run(debug=True)