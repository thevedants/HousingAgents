from google import genai
from google.genai import types
import pathlib
import httpx

client = genai.Client()

# Retrieve and encode the PDF byte
filepath = pathlib.Path('Path to CACI template pdf; relevant.pdf')

prompt = "Can you give me the exact format for the jury instructions form. The case is as follows: I, Robert, tried to pay my due rent to the landlord, Jeffrey, however he refused to take the payment and is now evictin me. Can you give me the exact format for the most relevant form here and fill it in with the required names. Can you also highlight the updates you make to the form. Don't hallucinate; Give me the exact format from the PDF."
response = client.models.generate_content(
  model="models/gemini-2.0-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)