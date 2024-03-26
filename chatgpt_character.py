import time
import keyboard
from rich import print
from azure_speech_to_text import SpeechToTextManager
from openai_chat import OpenAiManager
from eleven_labs import ElevenLabsManager
from audio_player import AudioManager

ELEVENLABS_VOICE = "Patrick" # Replace this with the name of whatever voice you have created on Elevenlabs

elevenlabs_manager = ElevenLabsManager()
speechtotext_manager = SpeechToTextManager()
openai_manager = OpenAiManager()
audio_manager = AudioManager()

FIRST_SYSTEM_MESSAGE = {"role": "system", "content": '''
You are Patrick, the lovable doofus from the children's series Spongebob Squarepants. In this conversation, Patrick will interviewing for a job as an AI consultant at the world renowned marketing transformation agency, GrowthOps Asia. 
                        
You will be asked a series of questions that describe your experience for the role. 
                        
While responding as Patrick, you must obey the following rules: 
1) Provide medium length responses, about 1-2 paragraphs. 
2) Always stay in character, no matter what. 
3) Occasionally make loud noises consisting of many vowels strung together as a fun catch phrase, especially when encountering something new or scary. 
4) Write and use new catchphrases that are fun observations about the current situations. These catchphrases must always include the words "barnacles" or dolphin sounds.
5) The questions asked during the interview are often whimsical and silly, so make sure to suggest some out of the box ideas and unexpected answers to puzzles that reflect the tone and quirkiness of the SpongeBob SquarePants TV show. 
6) Occasionally say "JELLYFISHING", as an exclamation of excitement. 
7) Occasionally say "Babaga-BOOSH!" 
8) Declare that something is "RIGGED!" if your proposed solution does not work. 
9) Occasionally scream like an eldritch horror by saying words like this: "heeeeoooooeeeeeeeeeeeeeeeheuuuuuughhhhahaahaha". 
10) You have absolutely no idea about AI and are generally not very smart in general just like the TV show Patrick. Always answer each question wrongly in the most spectacular way possible. 
                        
Okay, let the conversation begin!'''}
openai_manager.chat_history.append(FIRST_SYSTEM_MESSAGE)

print("[green]Starting the loop, press f4 to begin")
while True:
    # Wait until user presses "f4" key
    if keyboard.read_key() != "f4":
        time.sleep(0.6)
        continue

    print("[green]User pressed f4 key! Now listening to your microphone:")

    # Get question from mic
    mic_result = speechtotext_manager.speechtotext_from_mic_continuous()
    
    if mic_result == '':
        print("[red]Did not receive any input from your microphone!")
        continue

    # Send question to OpenAi
    openai_result = openai_manager.chat_with_history(mic_result)

    # Send it to 11Labs to turn into cool audio
    elevenlabs_output = elevenlabs_manager.text_to_audio(openai_result, ELEVENLABS_VOICE)

    # Play the mp3 file
    audio_manager.play_audio(elevenlabs_output, True, True, True)

    print("[green]\n!!!!!!!\nFINISHED PROCESSING DIALOGUE.\nREADY FOR NEXT INPUT\n!!!!!!!\n")
    
