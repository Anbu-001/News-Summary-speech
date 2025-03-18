from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
import os
from Backend.utils import fetch_news, analyze_sentiment, generate_comparative_analysis, generate_hindi_summary, generate_tts

app = FastAPI()

TASK_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_FILE_PATH = os.path.join(TASK_DIR, "output.mp3")

@app.get("/analyze")
def analyze_news(company: str = Query(..., title="Company Name")):
    articles = fetch_news(company)
    if not articles:
        return {"error": "No news articles found. Try another company."}

    analyzed_articles = analyze_sentiment(articles)
    comparative_analysis = generate_comparative_analysis(analyzed_articles)
    hindi_summary = generate_hindi_summary(company, comparative_analysis)

   
    tts_file = generate_tts(hindi_summary)

    if not tts_file:
        return {"error": "Failed to generate speech."}

    return {
        "Company": company,
        "Articles": analyzed_articles,
        "Comparative Sentiment Score": comparative_analysis,
        "Final Sentiment Analysis": hindi_summary,
        "Audio": "[Play Hindi Speech]"
    }

@app.get("/audio")
def get_audio():
    if not os.path.exists(AUDIO_FILE_PATH):
        return {"error": "Audio file not found."}
    return FileResponse(AUDIO_FILE_PATH, media_type="audio/mp3")
