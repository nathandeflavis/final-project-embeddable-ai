#Task 6
#1. Create the server.py file from scratch.
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

#2. Make sure that the Flask decorator for the application calling function is \emotionDetector.
@app.route("/emotionDetector")
def em_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    #3. Display the output in the specified format.
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    output = "For the given statement, the system response is "
    output += f"'anger': {anger}, "
    output += f"'disgust': {disgust}, "
    output += f"'fear': {fear}, "
    output += f"'joy': {joy} and "
    output += f"'sadness': {sadness}. "
    output += f"The dominant emotion is {dominant_emotion}."
    return output

@app.route("/")
def render_index_page():
    return render_template('index.html')

#4. Application needs to be deployed on localhost:5000
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)