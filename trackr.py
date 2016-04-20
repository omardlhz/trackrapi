from flask import Flask, request, jsonify
from youtube import youtube_search
import youtube_dl

application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello idiots!</h1>"

@application.route('/search')
def api_search():
    if 'name' in request.args:
       id = youtube_search(request.args['name'])
       ydl_opts = {'format': '140'}
       with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(id, download=False)
       return jsonify(url=result['url'], duration=result['duration'])

if __name__ == "__main__":
    application.run(host='0.0.0.0')
