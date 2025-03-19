# 📰 News Summarization & Sentiment Analysis

🚀 A web-based application that fetches news articles, performs sentiment analysis, generates a comparative summary, and converts it to Hindi speech using an AI-driven TTS model.

## 📌 Introduction  
This project extracts key details from **news articles** related to a company, analyzes their sentiment, conducts a **comparative analysis**, and generates a **Hindi text-to-speech (TTS) summary**. The application consists of:  
- A **FastAPI backend** for news fetching, sentiment analysis, and TTS generation.  
- A **Streamlit frontend** for user interaction.  
- Deployment on **Hugging Face Spaces** for easy access.  

## 🚀 Features  
✅ Scrapes **non-JS-based** news articles using `BeautifulSoup`.  
✅ Performs **Sentiment Analysis** using `nlptown/bert-base-multilingual-uncased-sentiment`.  
✅ Generates a **comparative summary** of news sentiment trends.  
✅ Converts the summary to **Hindi speech** using `gTTS`.  
✅ Fully deployed on **Hugging Face Spaces** with frontend-backend integration.  

## ⚙️ Project Setup

### 🔹 1. Clone the Repository  
```
git clone https://github.com/Anbu-001/News-Summary-speech.git
cd  News-Summary-speech
```

### 🔹 2. Install Dependencies  
```
pip install -r requirements.txt  
```


### 🔹 3. Run Backend Server  
```
cd backend  
uvicorn main:app --host 0.0.0.0 --port 8000 --reload  
```
The backend should now be accessible at:  
👉 `http://127.0.0.1:8000/docs`  

### 🔹 4. Run Frontend Application  
```
cd frontend  
streamlit run app.py  
```
The frontend should be running at:  
👉 `http://localhost:8501/`  

## 🧠 Model Details  

### 1️⃣ News Summarization  
- **Method:** Extracts the first few lines of each article as a summary.  
- **Library Used:** BeautifulSoup for web scraping.  

### 2️⃣ Sentiment Analysis  
- **Model:** `nlptown/bert-base-multilingual-uncased-sentiment` (Multilingual BERT).  
- **Purpose:** Classifies articles as **Positive, Neutral, or Negative** based on sentiment.  

### 3️⃣ Text-to-Speech (TTS)  
- **Library:** `gTTS (Google Text-to-Speech)`  
- **Purpose:** Converts **Hindi summary** into **audio speech (`output.mp3`)**.  

---

## 🛠 API Development  
The application provides **REST APIs using FastAPI**.  

### 📌 Access API Documentation  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

### 🔹 Available Endpoints  

| Method | Endpoint  | Description  | Query Parameters |
|--------|----------|-------------|-----------------|
| GET    | `/analyze`  | Fetches and analyzes news articles | `company=Tesla` |
| GET    | `/audio` | Returns generated Hindi speech | N/A |

---


---

## 🔗 API Usage (Third-Party Integrations)  
The application integrates **third-party APIs**:  

| Service | Purpose | Integration |
|---------|---------|------------|
| **The Guardian API** | Fetches news articles | `requests.get(url)` |
| **Hugging Face Transformers** | Sentiment Analysis | `transformers.pipeline` |
| **gTTS (Google Text-to-Speech)** | Converts Hindi text to speech | `gTTS(text, lang="hi")` |

---

## 📌 Assumptions & Limitations  

### ✅ Assumptions  
- News articles are available in **English** (since The Guardian API is used).  
- Sentiment labels are **mapped** from **1-star to 5-star ratings** to **Positive/Negative/Neutral**.  

### ⚠️ Limitations  
- **JavaScript-based** news pages **cannot be scraped** (BeautifulSoup works only with **static** pages).  
- **Hindi speech accuracy** depends on `gTTS`, which may not handle **complex sentences** well.  
- **API Rate Limits:** The Guardian API may restrict the **number of free requests**.  


