''' Executing this function initiates the application of sentiment
    analysis given a text.
'''
import json
import requests

def sentiment_analyzer(text_to_analyze):
    ''' This function recieves text and runs it through the Watson
        AI library to output sentiment label and score for given
        text.
    '''
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/ \
    watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header, timeout=3)
    if response.status_code == 500:
        return {'label':None,'score':None}
    label = json.loads(response.text)['documentSentiment']['label']
    score = json.loads(response.text)['documentSentiment']['score']
    return {'label':label,'score':score}
