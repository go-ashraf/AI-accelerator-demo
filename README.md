# GO-AI-INTERVIEW-PATRICK-DEMO
Simple app that lets you have a verbal conversation with OpenAi's GPT 3.5-Turbo to simulate an interview with the cartoon Patrick Star.
Modified from Babagaboosh by DougDoug. https://github.com/DougDougGithub/Babagaboosh

If you would like a crappy video explanation of this project, DougDoug made a video covering the basics here: https://www.youtube.com/watch?v=vYE1rkIMj9w

## SETUP:
1) This was written in Python 3.12.2.

2) Run `pip install -r requirements.txt` to install all modules.

3) This uses the Microsoft Azure TTS, Elevenlabs, and OpenAi services. You'll need to set up an account with these services and generate an API key from them. Then add these keys as windows environment variables named AZURE_TTS_KEY, AZURE_TTS_REGION, ELEVENLABS_API_KEY, and OPENAI_API_KEY respectively.

4) This app uses the GPT-3.5-Turbo model from OpenAi.

5) Optionally, you can use OBS and an OBS plugin to make images move while talking. First open up OBS. Install the Move OBS plugin: https://obsproject.com/forum/resources/move.913/ Now you can use this plugin to add a filter to an audio source that will change an image's transform based on the audio waveform. For example, I have this filter on a specific audio track that will move Patricks's image whenever text-to-speech audio is playing in that audio track.

6) Elevenlabs is the service I use for Ai voices. Once you've made an Ai voice on the Elevenlabs website, open up chatgpt_character.py and replace the ELEVENLABS_VOICE variable with the name of your Ai voice.

## Using the App

1) Run `chatgpt_character.py'

2) Once it's running, press F4 to start the conversation, and Azure Speech-to-text will listen to your microphone and transcribe it into text.

3) Once you're done talking, press P. Then the code will send all of the recorded text to the Ai. Note that you should wait a second or two after you're done talking before pressing P so that Azure has enough time to process all of the audio.

4) Wait a few seconds for OpenAi to generate a response and for Elevenlabs to turn that response into audio. Once it's done playing the response, you can press F4 to start the loop again and continue the conversation.
