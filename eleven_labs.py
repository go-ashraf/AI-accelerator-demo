from elevenlabs import generate, set_api_key, voices, save
import time
import os

try:
  set_api_key(os.getenv('ELEVENLABS_API_KEY'))
except TypeError:
  exit("Ooops! You forgot to set ELEVENLABS_API_KEY in your environment!")

class ElevenLabsManager:

    def __init__(self):
        # CALLING voices() IS NECESSARY TO INSTANTIATE 11LABS FOR SOME FUCKING REASON
        all_voices = voices()
        print(f"\nAll ElevenLabs voices: \n{all_voices}\n")

    # Convert text to speech, then save it to file. Returns the file path
    def text_to_audio(self, input_text, voice, subdirectory=""):
        audio_saved = generate(
          text=input_text,
          voice=voice,
          model="eleven_monolingual_v1"
        )
        file_name = f"___Msg{str(hash(input_text))}.mp3"
        tts_file = os.path.join(os.path.abspath(os.curdir), subdirectory, file_name)
        save(audio_saved,tts_file)
        return tts_file


if __name__ == '__main__':
    elevenlabs_manager = ElevenLabsManager()

    time.sleep(30)
