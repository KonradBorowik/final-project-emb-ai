''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import (
    Flask,
    render_template,
    request
)

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detection")


@app.route('/emotionDetector')
def detect_emotion() -> str:
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze: str = request.args.get('textToAnalyze')
    response: dict = emotion_detector(text_to_analyze)

    if response['dominant_emotion']:
        return f"For the given statement, the system response is \
                        'anger': {response['anger']}, \
                        'disgust': {response['disgust']}, \
                        'fear': {response['fear']}, \
                        'joy': {response['joy']}, \
                        'sadness': {response['sadness']}. \
                        The dominant emotion is {response['dominant_emotion']}."

    return "Invalid text! Please try again!"


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
