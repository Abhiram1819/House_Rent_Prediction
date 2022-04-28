from flask import Flask, render_template, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    localityId = request.form['localityId']
    bathroom = int(request.form['bathroom'])
    floor = int(request.form['floor'])
    parking = int(request.form['parking'])
    property_size = float(request.form['property_size'])
    type_bhk = int(request.form['type_bhk'])
    maintenance = int(request.form['maintenance'])

    response = jsonify({
        'estimated_price': util.predict_rent(localityId, bathroom, floor, parking, property_size, type_bhk, maintenance)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
