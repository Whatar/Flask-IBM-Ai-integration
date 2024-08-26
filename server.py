"""
server.py

This module sets up a Flask web application with routes for emotion detection.
"""


from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the index page.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Detect the emotion from the statement provided via GET request.
    """
    statement = request.args.get('statement')

    result = emotion_detector(statement)
    anger = result.get("anger", 0)
    disgust = result.get("disgust", 0)
    fear = result.get("fear", 0)
    joy = result.get("joy", 0)
    sadness = result.get("sadness", 0)
    dominant_emotion = result.get("dominant_emotion", "None")

    response_str = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    if not statement:
        response_str = "Invalid text! Please try again."
    return response_str


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
