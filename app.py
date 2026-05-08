import google.generativeai as genai
from dotenv import load_dotenv
import os

from prompts import SYSTEM_PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-8b")

question = input("Enter your question: ")

full_prompt = SYSTEM_PROMPT + "\n\nUser question:\n" + question

response = model.generate_content(full_prompt)

print("\nGenerated SQL:\n")
print(response.text)