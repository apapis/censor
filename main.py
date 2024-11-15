import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_data(url):
    try:
        response = requests.get(url)
        return response.text if response.status_code == 200 else None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
    
def main():
    api_url = os.getenv('API_URL')
    data=fetch_data(api_url)

    if data:
        print(data)

if __name__ == "__main__":
    main() 