import os
from dotenv import load_dotenv
import sys
sys.path.insert(0, 'E:/JUET/Projects/sonus/code/sonus-av-lib')
from sonus_av import AudioProcessor, ImageProcessor

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
def main():
    # Example usage of AudioProcessor
    print("Demonstrating AudioProcessor:")
    audio_proc = AudioProcessor()
    recognized_text = audio_proc.capture()
    print(f"Recognized Text: {recognized_text}\n")

    # Example usage of ImageProcessor
    print("Demonstrating ImageProcessor:")
    image = os.environ.get("IMAGE_URL")
    image_proc = ImageProcessor(api_key=api_key)
    image_description = image_proc.describe_image(image)
    print(f"Image Description: {image_description}\n")

if __name__ == "__main__":
    main()
