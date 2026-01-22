import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
print("genai version:", getattr(genai, "__version__", "unknown"))

model = genai.GenerativeModel("gemini-2.0-flash")
resp = model.generate_content("Say hello, this is a test from Priyanshu.")
print(resp.text)
