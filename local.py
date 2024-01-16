import base64
import requests

# OpenAI API Key
api_key = "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"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "./graph9.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          # Previous prompt: What's in the image?
          "text": "Please describe the following graph, table, or engineering diagram. Identify all key components, but keep it within 2-3 sentences maximum. In addition, please provide a full thought on the image without cutting the response abruptly."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())