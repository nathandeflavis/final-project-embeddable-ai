import requests

#3. Write the function to run emotion detection using the appropriate Emotion Detection function.
#Name this function emotion_detector.
#Assume that that text to be analyzed is passed to the function as an argument and is stored in the variable text_to_analyze.
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = json, headers = headers)
    #The value being returned must be the text attribute of the response object as received from the Emotion Detection function.
    return response.text