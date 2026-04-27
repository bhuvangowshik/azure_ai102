import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
 
ENDPOINT = os.getenv("AZURE_LANGUAGE_ENDPOINT")
KEY = os.getenv("AZURE_LANGUAGE_KEY")
 
def get_client():
    return TextAnalyticsClient(
        endpoint=ENDPOINT,
        credential=AzureKeyCredential(KEY)
    )
 
# Detect language + sentiment
def analyze_texts(texts):
    client = get_client()
 
    lang_results = client.detect_language(texts)
    sentiment_results = client.analyze_sentiment(texts)
 
    output = []
 
    for i in range(len(texts)):
        lang = lang_results[i].primary_language.name
        sentiment = sentiment_results[i].sentiment
 
        scores = sentiment_results[i].confidence_scores
 
        output.append({
            "text": texts[i],
            "language": lang,
            "sentiment": sentiment,
            "positive": scores.positive,
            "neutral": scores.neutral,
            "negative": scores.negative
        })
 
    return output
