import http.client
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def fetch_data():
    conn = http.client.HTTPSConnection("free-vpn.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "73b648ba38msh3e089d744949716p15fca1jsn98003b17d294",
        'x-rapidapi-host': "free-vpn.p.rapidapi.com"
    }
    conn.request("GET", "/get_vpn_data", headers=headers)
    res = conn.getresponse()
    data = res.read()
    vpn_data = data.decode("utf-8")
    
    return jsonify(vpn_data)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
