import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import os
from dotenv import load_dotenv

# API anahtarlarını yükle
load_dotenv()
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Sentiment Analyzer'i başlat
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Twitter API'ye bağlan
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Arama sorgusu: Fenerbahçe hashtag'i, retweetler hariç, Türkçe dilinde
query = "#Fenerbahçe -is:retweet lang:tr"

# 100 tweet çek
tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["text"])

# Tweet verilerini saklamak için liste
data = []

if tweets.data:
    for tweet in tweets.data:
        text = tweet.text
        sentiment_score = sia.polarity_scores(text)['compound']
        sentiment = "Pozitif" if sentiment_score > 0.05 else "Negatif" if sentiment_score < -0.05 else "Nötr"
        data.append([text, sentiment_score, sentiment])

    # Veriyi DataFrame'e çevir
    df = pd.DataFrame(data, columns=["Tweet", "Sentiment Score", "Sentiment"])

    # Duygu dağılımını görselleştir
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df["Sentiment"], hue=df["Sentiment"], palette="viridis", legend=False)
    plt.title("Tweet Sentiment Dağılımı")
    plt.xlabel("Duygu")
    plt.ylabel("Tweet Sayısı")
    plt.show()

    # Analiz sonuçlarını CSV olarak kaydet
    df.to_csv("tweet_sentiment_analysis.csv", index=False)
    print("Analiz tamamlandı ve CSV dosyası kaydedildi.")
else:
    print("Tweet bulunamadı veya API erişimi kısıtlı.")
