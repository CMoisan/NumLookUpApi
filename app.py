import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "num_live_wUktAqcbd7KHQB3zoaUnTjUxl8ibyxNhT2VdNwXy"
API_URL = "https://api.numlookupapi.com/v1/validate/"

@app.route('/verify', methods=['GET'])
def verify_number():
    phone_number = request.args.get('number')
    country_code = request.args.get('country_code', 'FR')

    if not phone_number:
        return jsonify({"error": "Numéro de téléphone requis"}), 400

    full_api_url = f"{API_URL}{phone_number}?apikey={API_KEY}&country_code={country_code}"

    print(f"URL complète de l'API : {full_api_url}")

    try:
        response = requests.get(full_api_url)

        print(f"Code de statut HTTP : {response.status_code}")
        print(f"Réponse brute : {response.text}")

        if response.status_code != 200:
            return jsonify({"error": f"Erreur {response.status_code}: {response.text}"}), response.status_code

        data = response.json()

        return jsonify({
            "valid": data.get("valid"),
            "number": data.get("international_format"),
            "carrier": data.get("carrier"),
            "location": data.get("location"),
            "type": data.get("line_type")
        })

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Erreur de connexion à l'API", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
