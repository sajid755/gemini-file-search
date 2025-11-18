"""
Shared configuration for Gemini File Search API
"""
import os
from dotenv import load_dotenv
import google.genai as genai

# Load environment variables
load_dotenv()

# Get API key
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Default model for queries
DEFAULT_MODEL = "gemini-2.0-flash-exp"
