# Sonus-AV

## Description
Sonus-AV is a Python library designed to enhance Large Language Models (LLMs) by adding support for voice and image inputs. This library simplifies the process of converting speech to text and analyzing images before feeding the information to LLMs.

## Features
- **Audio Processing**: Convert audio input to text using `AudioProcessor`, which supports multiple languages and can handle real-time translation.
- **Image Processing**: Use `ImageProcessor` to extract text from images or generate descriptions of images using advanced machine learning models.

## Installation

Install the library using pip:

```bash
pip install sonus-av
```

## Usage

### Audio Processing
Here is how you can use the `AudioProcessor` to convert speech to text:

```python
from sonus_av import AudioProcessor

# Initialize the processor
audio_processor = AudioProcessor()

# Capture and translate audio to text
recognized_text = audio_processor.capture('path_to_your_audio_file.wav')
print(recognized_text)
```

### Image Processing
Here is how you can use the `ImageProcessor` to get a description of an image:

```python
from sonus_av import ImageProcessor

# Initialize the processor with your OpenAI API key
image_processor = ImageProcessor(api_key='your-openai-api-key')

# Get an image description
image_description = image_processor.describe_image(image_path)
print(image_description)
```

## Contributions
Contributions are welcome! Please fork the repository and open a pull request with your improvements.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
