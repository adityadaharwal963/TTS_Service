"""
This file define flask server and api 

api docs:

@get
path /success/
function : To check system is working

@post 
path /tts/
function : Convert text to speech for audio msg

"""

from flask import Flask, send_file, request
from flask_cors import CORS
# from model.src.tts_mac import text_to_speech


app = Flask(__name__)
CORS(app)

@app.route('/check')
def success():
    """
    Endpoint checking health of server
    """
    return 'welcome'


# @app.route('/tts/', methods=['POST'])
# def text_speech():
#     """
#     Endpoint for generating speech from text
#     """
#     if request.method == 'POST':
#         data = request.get_json()
#         print(data['text'])
#         text = data['text']
#         text_to_speech(text)
#         mp3_path = "test1.mp3"
#         return send_file(mp3_path, as_attachment=True, download_name='my_audio.mp3', mimetype='audio/mpeg')
#         # return text

if __name__ == '__main__':
    app.run(port=8000)