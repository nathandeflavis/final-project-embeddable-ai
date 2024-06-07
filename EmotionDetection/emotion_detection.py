import json
import requests

#Task 2: 3. Write the function to run emotion detection using the appropriate Emotion Detection function.
#Name this function emotion_detector.
#Assume that that text to be analyzed is passed to the function as an argument and is stored in the variable text_to_analyze.
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = headers)
    #Task 3: 1. Convert the response text into a dictionary using the json library functions.
    formatted_response = json.loads(response.text)
    #Task 7: 1. Access the status_code attribute of the server response to correctly display the system response for blank entries.
    #For status_code = 400, make the function return the same dictionary, but with values for all keys being None.
    formatted_output = {}

    if response.status_code == 400:
        keys = formatted_response.keys()

        for key in keys:
            formatted_output[key] = None

        formatted_output['dominant_emotion'] = None
    else:
        #Task 3: 2. Extract the required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores.
        emotion_predictions = (formatted_response['emotionPredictions'])[0]
        emotion_scores = emotion_predictions['emotion']
        #Task 3: 3. Write the code logic to find the dominant emotion, which is the emotion with the highest score.
        dominant_emotion = get_dominant_emotion(emotion_scores)
        #Task 3: 4. modify the emotion_predictor [sic] function to return the specified output format
        formatted_output = dict(emotion_scores)
        formatted_output['dominant_emotion'] = dominant_emotion
    return formatted_output

def get_dominant_emotion(emotion_scores):
    emotion_score_max = 0
    dominant_emotion = None
    keys = emotion_scores.keys()

    for key in keys:
        value = emotion_scores[key]

        if value > emotion_score_max:
            emotion_score_max = value
            dominant_emotion = key
    
    return dominant_emotion