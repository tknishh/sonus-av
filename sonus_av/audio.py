import speech_recognition as sr
from deep_translator import GoogleTranslator
from google.transliteration import transliterate_text

class AudioProcessor:
    def __init__(self, input_lang='auto', output_lang='en'):
        self.input_lang = input_lang
        self.output_lang = output_lang
        self.recognizer = sr.Recognizer()

    def capture(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)

            try:
                # Recognize speech using Google's speech recognition
                recognized_text = self.recognizer.recognize_google(audio, language=self.input_lang)
                print(f"Recognized (original): {recognized_text}")

                # Translate to English
                if self.output_lang != 'en':
                    speech_text = transliterate_text(recognized_text, lang_code='en')
                    translated_text = GoogleTranslator(source=self.input_lang, target=self.output_lang).translate(text=speech_text)
                    print(f"Translated to English: {translated_text}")
                    return translated_text
                return recognized_text
            except sr.UnknownValueError:
                return "Could not understand the audio."
            except sr.RequestError:
                return "Failed to request translation."

    def translate_text(self, text):
        return GoogleTranslator(source=self.input_lang, target='en').translate(text=text)