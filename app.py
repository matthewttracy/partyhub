from flask import Flask, jsonify, request, send_from_directory
app = Flask(__name__)
############################

musicqueue = []
next_id = 0

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/display")
def display():
    return send_from_directory("static", "display.html")



@app.route("/queue", methods=['GET', 'POST'])
def queue():
    # allow global variable access
    global next_id

    # determine if POST or GET 
    if(request.method == 'GET'):
        return jsonify(musicqueue)
    else:
        songjson = request.json
        #validating input
        if(songjson.get('title') == '' or songjson.get('artist') == ''):
            return jsonify({"error": "missing data"}), 400
        else:
            # creating dictionary for new song 
            newsong = {"id": next_id, "title": songjson.get('title'), "artist": songjson.get('artist')}
            musicqueue.append(newsong)
            next_id += 1
            return "Song added to queue"


#remove item 
@app.route("/queue/<int:queue_id>", methods=["DELETE"])
def remove_song(queue_id):
    for song in musicqueue:
        if (song["id"] == queue_id):
            musicqueue.remove(song)
            return "song removed - 200"
    # else 
    return "no song found to remove - 404"


#skip item
@app.route("/queue/skip", methods = ["POST"])
def skip_song():
    try:
        musicqueue.pop(0)
        return "skipped song - 200"
    except IndexError:
        return "no song to skip - 404"
