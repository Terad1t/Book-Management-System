from flask import Flask, render_template, abort, jsonify, request
from api.database import criar_tabelas
from api.routes.v1 import api_v1

app = Flask(__name__)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

@app.errorhandler(400)
def bad_request(e):
    return jsonify({'error': 'Bad request', 'message': e.description}), 400

criar_tabelas()
app.register_blueprint(api_v1)

if __name__ == "__main__":
    app.run(debug=True)
