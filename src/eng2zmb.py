import random
import pyaudio
import numpy as np
import whisper
# import torch
# import time
# from dotenv import load_dotenv
# import os
from .datatypes.lexicon import *

print("\033[H\033[J", end="")
print("Welcome to Zombie Translator(ENG to ZMB)")
print("The apocalypse is here. The zombies are coming. You are the last hope of humanity.")
print("You, having perfect pitch have realized that zombies speak in musical grunts.")
print("Interested in their language, you've created a translator in an attempt to communicate with them.")
print("Especially for the Toronto Zombies, speak into the mic with Toronto Slang, and we will do our best to translate.")
print("")

def string_to_list(input_string):
    # Remove the surrounding square brackets
    input_string = input_string.strip('[]')
    
    # Split the string by ', ' and remove the single quotes
    list_elements = [element.strip().strip("'") for element in input_string.split(',')]
    
    return list_elements

ZombieNotes = []  # Define ZombieNotes list in a global scope
def toronto_conversion():
    word = ""
#    print(toronto_text[0])
    for i in range(len(toronto_text)):
        if toronto_text[i] in list(OpenersReverse().keys()):
            word = OpenersReverse()[toronto_text[i]]
            ZombieNotes.append(OpenersReverse()[toronto_text[i]])
        elif toronto_text[i] in SubjectsReverse().keys():
            word = SubjectsReverse()[toronto_text[i]]
            ZombieNotes.append(SubjectsReverse()[toronto_text[i]])
        elif toronto_text[i] in VerbsReverse().keys():
            word = VerbsReverse()[toronto_text[i]]
            ZombieNotes.append(VerbsReverse()[toronto_text[i]])
        elif toronto_text[i] in ObjectsReverse().keys():
            word = ObjectsReverse()[toronto_text[i]]
            ZombieNotes.append(ObjectsReverse()[toronto_text[i]])
        elif toronto_text[i] in ClosersReverse().keys():
            word = ClosersReverse()[toronto_text[i]]
            ZombieNotes.append(ClosersReverse()[toronto_text[i]])
        else:
            # print("Error: Word not found in dictionary, utilizing placeholder!")
            word = random.choice(list(OpenersReverse().values()))
            ZombieNotes.append(random.choice(list(OpenersReverse().values())))
        # print(word)
#    print(toronto_text)
# ZombieNotes = []  # Define ZombieNotes list in a global scope

        

# Load the Whisper model
model = whisper.load_model("base")

# Parameters for the audio recording
FORMAT = pyaudio.paInt16  # Format of sampling (16-bit PCM)
CHANNELS = 1              # Number of channels (mono)
RATE = 16000              # Sampling rate (16 kHz for Whisper compatibility)
CHUNK = 1024              # Number of frames per buffer
CHUNKS_PER_SECOND = RATE // CHUNK
BUFFER_SIZE_SECONDS = 5
BUFFER_SIZE = CHUNKS_PER_SECOND * BUFFER_SIZE_SECONDS

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open a stream with the above parameters
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Listening...")

# Initialize a buffer to hold audio data
audio_buffer = np.zeros(BUFFER_SIZE * CHUNK, dtype=np.float32)

#print("-----", OpenersReverse()["whazzgood"])
#print(ObjectsReverse())
try:
    while True:
        OpenersReverse()
        # Read audio data from the stream
        for i in range(BUFFER_SIZE):
            data = stream.read(CHUNK)
            audio_chunk = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
            audio_buffer[i * CHUNK:(i + 1) * CHUNK] = audio_chunk

        # Convert the audio buffer to the format expected by Whisper
        audio_buffer = audio_buffer.astype(np.float32)

        # Transcribe the audio data
        result = model.transcribe(audio_buffer, fp16=False)

        # Print the transcribed text
        from openai import OpenAI
        # load_dotenv()
        client = OpenAI(api_key="56SIJW3HWYD8YZNJYRMKB7N1372RX70WPVQ7O11U18HZCJEW1VL4RORMYTTPY5YD",base_url="https://jamsapi.hackclub.dev/openai/")
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": "I will provide you a dictionary. They are specifically words of a venacular from Toronto. You will NOT take into consideration, the meaning. You will NOT use words not present in the dictionary. In the event you can NOT figure out the word, pick a word from the dictionary to fill it's place. You will have the same number of words in the output as in the input, UNLESS the output has words that represent compound words/phrases.  The output MUST result in 5 words. No punctation, no capital letters. Format the output as a python list. You will try to take my input sentence and format it  based on sound, to the words in my dictionary. For example, You Don't Know, becomes You Dun Know. Dictionary: Whazzgood Hol’up Yo Nah-fam Straight-up Real talk Wagwan We out here Slime Fam Big Man Mandem Bredrin Plug Ting Galdem Ends Whip Cheese Drip Water Brains We Dawg Homie Is runnin link holla Whippin chirpin’ flexin’ Catch-a-vibe Settle Run Skrrt Swerve Run up Chop Mash up Could gyat Whip 6ix Cheese Slime Yute Ting Drip Food Watah Raps Gwop Block Piff G Ends Deadass No cap Facts Bless up Boom Safe Trust On god Say less You dun know Clapped On job]"
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": result['text']
                }
            ]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        # Torontoed Text!
#        print(response.choices)
 #       print(response.choices[0].message.content)
        try:

            toronto_text = string_to_list(response.choices[0].message.content)
        except:
            print("Error: No text found")
#        print(toronto_text)
        toronto_conversion()
#        print("Zombie Text: ", ZombieNotes)
#        print(ZombieNotes[0])
        # Play Audio
        from playsound import playsound
        
        print("Zombie Translation Playing Now")
        playsound(ZombieNotes[0])
        playsound(ZombieNotes[1])
        playsound(ZombieNotes[2])
        playsound(ZombieNotes[3])  
        playsound(ZombieNotes[4])
        print("Run Again for More Translations")

        break
    


            # Sleep for a while to simulate real-time processing (optional)
        # time.sleep(BUFFER_SIZE_SECONDS)

except KeyboardInterrupt:
    print("Stopping...")

# Stop and close the stream
stream.stop_stream()
stream.close()
p.terminate()
