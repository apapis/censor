import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

def fetch_data(url):
    try:
        response = requests.get(url)
        return response.text if response.status_code == 200 else None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def process_with_ai(text):
    instruction = f"""Given exactly this text, replace sensitive data with CENZURA:

Text to process: {text}

Rules for replacement:
- Replace names and surnames with CENZURA
- Replace ages with CENZURA
- Replace cities with CENZURA
- Replace streets with numbers with CENZURA

EXACT EXAMPLE:
If input is: "Podejrzany: Krzysztof Kwiatkowski. Mieszka w Szczecinie przy ul. Różanej 12. Ma 31 lat."
You must output: "Podejrzany: CENZURA. Mieszka w CENZURA, przy ul. CENZURA. Ma CENZURA lat."

Output the processed text directly, without any JSON, without any explanation, without any additional formatting.
Start your response with the processed text immediately."""
    
    payload = {
        "model": "llama2:7b",
        "prompt": instruction,
        "temperature": 0,
        "stream": False
    }
    
    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        if response.status_code == 200:
            return response.json().get('response', '').strip()
    except requests.RequestException as e:
        print(f"AI Processing Error: {e}")
        return None

def main():
    api_url = os.getenv('API_URL')
    data = fetch_data(api_url)
    
    if data:
        censored_text = process_with_ai(data)
        print(data)
        print(censored_text)

if __name__ == "__main__":
    main()