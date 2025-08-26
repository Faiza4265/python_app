import os
from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def Profile():
	return render_template('faiza.html')
	
@app.route('/Place')
def Place():
	return 'Hello from Github repo'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # use Render's PORT or default to 5000
    app.run(host="0.0.0.0", port=port)

