import zipfile
import os
import base64
import requests
import tempfile
from imgcat import imgcat

class ImageProcessor:

    def __init__(self, api_key):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("OpenAI API key not found. Set the OPENAI_API_KEY environment variable.")

    def describe_image(self, image_path):
        encoded_image = self.encode_image(image_path)
        return self.get_caption(encoded_image, self.api_key)

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def get_caption(self, base64_image, api_key):
        custom_prompt = "Directly describe with brevity and as brief as possible the scene or characters without any introductory phrase like 'This image shows', 'In the scene', 'This image depicts' or similar phrases. Just start describing the scene please. Do not end the caption with a '.'. Some characters may be animated, refer to them as regular humans and not animated humans. Please make no reference to any particular style or characters from any TV show or Movie. Good examples: a cat on a windowsill, a photo of smiling cactus in an office, a man and baby sitting by a window, a photo of wheel on a car,"
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
                        {"type": "text", "text": custom_prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ]
                }
            ],
            "max_tokens": 300
        }

        try:
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            response.raise_for_status()
            response_json = response.json()

            if 'choices' in response_json and response_json['choices'] and 'message' in response_json['choices'][0]:
                caption = response_json['choices'][0]['message'].get('content', 'Caption not found').strip()
                # Remove commas and double quotes from the caption
                caption = caption.replace(',', '').replace('"', '')
                return caption
        except requests.RequestException as e:
            print(f"API request failed: {e}")
        return "Failed to get caption"

    def process_images(self, input_path, api_key):
        caption = ""
        with tempfile.TemporaryDirectory() as temp_dir:
            if os.path.isdir(input_path):
                directory_to_process = input_path
            elif zipfile.is_zipfile(input_path):
                with zipfile.ZipFile(input_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_dir)
                directory_to_process = temp_dir
            else:
                directory_to_process = os.path.dirname(input_path)

            for root, _, files in os.walk(directory_to_process):
                for file_name in filter(lambda f: f.lower().endswith(('.png', '.jpg', '.jpeg')), files):
                    image_path = os.path.join(root, file_name)
                    base64_image = self.encode_image(image_path)
                    caption = self.get_caption(base64_image, api_key)
                    imgcat(open(image_path, 'rb').read())
                    print(f"Caption: {caption}\n")
        return caption
