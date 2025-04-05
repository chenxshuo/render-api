import requests
import time
from datetime import datetime

# Replace this with your Render service URL when deploying
# BASE_URL = "http://localhost:8000"
BASE_URL = "https://render-api-82tt.onrender.com"

def test_health():
    """Test the health check endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print("\nHealth Check:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_send_text(text):
    """Test sending text to the API"""
    data = {"text": text}
    response = requests.post(f"{BASE_URL}/text", json=data)
    print(f"\nSending text: {text}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.json()

def test_get_texts():
    """Test retrieving all texts"""
    response = requests.get(f"{BASE_URL}/texts")
    print("\nRetrieving all texts:")
    print(f"Status Code: {response.status_code}")
    messages = response.json()
    for msg in messages:
        # Convert timestamp string to datetime for better formatting
        timestamp = datetime.fromisoformat(msg['timestamp'].replace('Z', '+00:00'))
        print(f"ID: {msg['id']}, Time: {timestamp}, Text: {msg['text']}")

def run_tests():
    # Test health endpoint
    test_health()
    
    # Test sending multiple messages
    test_send_text("Hello, this is my first message!")
    time.sleep(1)  # Add small delay between messages
    test_send_text("This is my second message.")
    time.sleep(1)
    test_send_text("And here's my third message!")
    
    # Test retrieving all messages
    test_get_texts()

if __name__ == "__main__":
    print("Starting API tests...")
    run_tests()
    print("\nTests completed!")
