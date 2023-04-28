# pip install --upgrade openai
# check github openai documentation for installing openai package
# pip install python-dotenv
# check https://pypi.org/project/python-dotenv/ for installing dotenv package
import json
import openai
from dotenv import dotenv_values
import sys

keys = dotenv_values(".env")
openai.api_key = keys['OPENAI_API_KEY']

try:
    keys = dotenv_values(".env")
    openai.api_key = keys["OPENAI_API_KEY"]
except KeyError:
    print("Please add/update your OpenAI API key to the .env file")
    sys.exit(1)


def playlist_generator(prompt, count=10):
    example_json = """
    [
    {"song": "Pink Noise Loop", "artist": "Calmsound"},
    {"song": "Sleep Sounds", "artist": "The Sleep Specialist"},
    {"song": "Deep Sleep", "artist": "Peder B. Helland"},
    {"song": "Sleep Music Delta Waves", "artist": "Meditation Relax Club"},
    {"song": "Pink Noise", "artist": "Sleepy Sounds"}
    ]"""

    messages = [
        {"role": "system", "content": """" You are a helpful playlist generating 
        assistant.I want you to generate a list of songs using a text prompt from
         a user. Return the playlist in a JSON array that follows this format:
        {"song: <song-title>, :artist: <artist-name>."""},
        {"role": "user", "content": """Generate a playlist of {count} songs and 
        their artist based on the following prompt: {prompt}"""},
        {"role": "assistant", "content": example_json},
    ]

    while True:
        try:
            response = openai.ChatCompletion.create(
                messages=messages,
                model="gpt-3.5-turbo",
                max_tokens=600,
            )
            playlist = json.loads(response["choices"][0]["message"]["content"])
            print(playlist)
            print("Total tokens used: " + str(response.usage["total_tokens"]))
        except KeyboardInterrupt:
            print("Quitting application...")
            break


# playlist_generator("Songs that promote deep sleep.", 50)

# playlist_generator("Songs for deep focus.", 20)
