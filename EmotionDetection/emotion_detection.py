''' Module that handles the emotion detection
'''
import json
import requests


def emotion_detector(text_to_analyze: str) -> dict:
    ''' Analyze the text and extract the emotion of it
    '''
    url: str = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # pylint: disable=C0301
    headers: dict = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data: dict = { "raw_document": { "text": text_to_analyze } }

    response: requests.Response = requests.post(
        url=url,
        headers=headers,
        json=input_data,
        timeout=10
    )
    formatted_response: dict = json.loads(response.text)

    if response.status_code == 200:
        emotions: dict = formatted_response['emotionPredictions'][0]['emotion']
    elif response.status_code == 400:
        emotions: dict = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
        }

    try:
        max_emotion_value: float = max(emotions.values())
        for emotion in emotions:
            if emotions[emotion] == max_emotion_value:
                emotions['dominant_emotion'] = emotion
                break
    except:
        emotions['dominant_emotion'] = None

    return emotions
