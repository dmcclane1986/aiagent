import os
from dotenv import load_dotenv
from google import genai
import sys

verbose = False

if len(sys.argv)<2:
    print("Please provide a prompt for the agent.")
    print("Usage: main.py 'Your prompt here' ")
    sys.exit(1)
elif len(sys.argv)>2:
    if sys.argv[2] == "--verbose":
        verbose = True

query = sys.argv[1]



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model = 'gemini-2.0-flash-001', 
    contents = query
)
if verbose:
    print(f"User prompt: {query}")
    print(response.text)

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    print(response.text)