''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    emotion = emotion_detector(text_to_analyse)
    emotion_predictions = str(dict(list(emotion.items())[:4]))

    return f"""\
For the given statement, the system response is {emotion_predictions[1:len(emotion_predictions)-1]} and 'sadness': {emotion['sadness']}. \
The dominant emotion is <b>{emotion['dominant_emotion']}</b>.
"""

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)
