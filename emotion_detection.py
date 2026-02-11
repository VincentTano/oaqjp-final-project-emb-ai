import requests, json

def emotion_detector(text_to_analyse: str = ""):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json={ "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=input_json, headers=headers)
    result = json.loads(response.text)
    emotion = result['emotionPredictions'][0]['emotion']
    emotion['dominant_emotion']=sorted(emotion,key=emotion.get,reverse=True)[0]

    return(emotion)