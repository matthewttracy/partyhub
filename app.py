from flask import Flask, jsonify, request
app = Flask(__name__)
############################

musicqueue = []

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/queue", methods=['GET', 'POST'])
def display():
    if(request.method == 'GET'):
        return jsonify(musicqueue)
    else:
        songjson = request.json
        #validating input
        if(songjson.get('title') == '' or songjson.get('artist') == ''):
            return jsonify({"error": "missing data"}), 400
        else:
            # creating dictionary for new song 
            newsong = {"Title": songjson.get('title'), "Artist": songjson.get('artist')}
            return newsong

    
