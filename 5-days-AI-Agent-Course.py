import os

try:
    # In Google Colab, you can directly set your API key
    # or use google.colab.userdata.get('GOOGLE_API_KEY') if stored as a secret.
    # For now, please replace 'YOUR_API_KEY_HERE' with your actual GOOGLE_API_KEY.
    GOOGLE_API_KEY = "YOUR_API_KEY_HERE" # Replace with your actual GOOGLE_API_KEY
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"
    print("✅ Gemini API key setup complete.")
except Exception as e:
    print(f"🔑 Authentication Error: Please ensure GOOGLE_API_KEY is correctly set. Details: {e}")
