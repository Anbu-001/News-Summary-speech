import requests
import os
import torch
import random
import torchaudio
from gtts import gTTS
import soundfile as sf
from pydub import AudioSegment
from transformers import pipeline


TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


sentiment_pipeline = pipeline("sentiment-analysis")


def fetch_news(company):
    
    api_key = "MY_Api_Key"
    url = f"https://content.guardianapis.com/search?q={company}&api-key={api_key}&show-fields=trailText"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = [
            {
                "Title": article["webTitle"],
                "Summary": article["fields"]["trailText"],
                "Sentiment": "Pending Analysis",
                "Topics": [company]  
            }
            for article in data["response"]["results"][:10]
        ]
        return articles
    else:
        return {"error": "Failed to fetch news"}



def analyze_sentiment(articles):
    for article in articles:
        sentiment_result = sentiment_pipeline(article["Summary"])[0]
        sentiment_label = sentiment_result["label"].capitalize()  
        article["Sentiment"] = sentiment_label
    return articles



def generate_comparative_analysis(articles):
    if len(articles) < 2:
        return {"error": "Not enough articles for comparison."}

    sentiment_distribution = {"Positive": 0, "Negative": 0, "Neutral": 0}
    coverage_differences = []

    for article in articles:
        sentiment_distribution[article["Sentiment"]] += 1

    for i in range(len(articles) - 1):
        coverage_differences.append({
            "Comparison": f"Article {i+1} discusses {articles[i]['Summary']}, while Article {i+2} focuses on {articles[i+1]['Summary']}.",
            "Impact": random.choice([
                "Investors may react positively.",
                "Stock prices might be affected.",
                "Company reputation could shift."
            ])
        })

    return {
        "Sentiment Distribution": sentiment_distribution,
        "Coverage Differences": coverage_differences
    }



def generate_hindi_summary(company, sentiment_data):
    
    if "Sentiment Distribution" not in sentiment_data:
        print("❌ Error: 'Sentiment Distribution' key not found in sentiment data.")
        return "❌ हिंदी सारांश बनाने में त्रुटि हुई।"

    summary = f"{company} के समाचार विश्लेषण का सारांश:\n"

    summary += f"🌟 सकारात्मक समाचार: {sentiment_data['Sentiment Distribution'].get('Positive', 0)} लेख\n"
    summary += f"⚠️ नकारात्मक समाचार: {sentiment_data['Sentiment Distribution'].get('Negative', 0)} लेख\n"
    summary += f"🔹 तटस्थ समाचार: {sentiment_data['Sentiment Distribution'].get('Neutral', 0)} लेख\n"

    
    if "Coverage Differences" in sentiment_data and isinstance(sentiment_data["Coverage Differences"], list):
        for i, diff in enumerate(sentiment_data["Coverage Differences"]):
            summary += f"📌 तुलना {i+1}: {diff.get('Comparison', 'जानकारी उपलब्ध नहीं')}\n"
            summary += f"🔍 प्रभाव: {diff.get('Impact', 'जानकारी उपलब्ध नहीं')}\n"

    return summary





def generate_tts(text, filename="output.mp3"):
    if not text.strip():
        print("❌ TTS Error: No text provided for speech generation.")
        return None

    try:
        
        tts = gTTS(text=text, lang="hi")
        tts.save(filename)
        print(f"✅ TTS generated successfully: {filename}")
        return filename
    except Exception as e:
        print(f"❌ TTS Error: {e}")
        return None





