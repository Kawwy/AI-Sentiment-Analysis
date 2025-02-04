import requests, json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = {
        "raw_document" : { "text" : text_to_analyse }
    }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    resp = requests.post(url, json = myobj, headers=header)
    formatted_resp = json.loads(resp.text)
    if resp.status_code == 200:
        label = formatted_resp['documentSentiment']['label']
        score = formatted_resp['documentSentiment']['score']
    elif resp.status_code == 500:
        label = None
        score = None
    return {"Label" : label, "Score" : score}