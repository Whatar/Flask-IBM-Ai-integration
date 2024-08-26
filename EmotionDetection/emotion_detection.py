import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)

    emotions = response.json()["emotionPredictions"][0]["emotion"]

    return {
        'anger': emotions["anger"],
        'disgust': emotions["disgust"],
        'fear': emotions["fear"],
        'joy': emotions["joy"],
        'sadness': emotions["sadness"],
        'dominant_emotion': max(emotions, key=emotions.get)
    }