from flask import Flask, jsonify
from flasgger import Swagger

import api

app= Flask(__name__)
Swagger(app)

@app.route('/api/<vargument>')

def flerpterp(arg):
	return jsonify({'arg':arg})

app.run()
