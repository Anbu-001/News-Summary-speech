import streamlit as st
import requests
import os

API_URL = "http://127.0.0.1:8000"

st.title("📰 News Summarization")

company_name = st.text_input("Enter company name", "Tesla")

if st.button("Analyze News"):
    with st.spinner("Fetching news and analyzing sentiment..."):
        response = requests.get(f"{API_URL}/analyze?company={company_name}")
        
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                st.error(data["error"])
            else:
                st.subheader(f"📊 Sentiment Analysis for {company_name}")
                st.json(data["Comparative Sentiment Score"])

                st.subheader("📄 Articles:")
                for idx, article in enumerate(data["Articles"]):
                    st.write(f"**{idx+1}. {article['Title']}**")
                    st.write(f"Summary: {article['Summary']}")
                    st.write(f"Sentiment: {article['Sentiment']}")

                st.subheader("📜 Hindi Sentiment Summary")
                st.write(data["Final Sentiment Analysis"])

                st.subheader("🔊 Listen to Summary in Hindi")
                audio_response = requests.get(f"{API_URL}/audio")

                if audio_response.status_code == 200:
                    audio_file = os.path.join(os.path.dirname(__file__), "../output.mp3")
                    if os.path.exists(audio_file):
                        st.audio(audio_file, format="audio/mp3")
                    else:
                        st.error("❌ Audio file not found.")
                else:
                    st.error("❌ Failed to load audio. Try again.")
        else:
            st.error("Failed to fetch news.")
