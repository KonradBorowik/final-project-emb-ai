import json
import requests


def emotion_detector(text_to_analyse: str) -> dict:
    url: str = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers: dict = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data: dict = { "raw_document": { "text": text_to_analyse } }

    response: requests.Response = requests.post(
        url=url,
        headers=headers,
        json=input_data
    )
    formatted_response: dict = json.loads(response.text)
    emotions: dict = formatted_response['emotionPredictions'][0]['emotion']

    return emotions
