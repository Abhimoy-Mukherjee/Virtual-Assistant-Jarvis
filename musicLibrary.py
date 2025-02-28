import speech_recognition as sr
import webbrowser
import os
import yt_dlp
import pygame
from pydub import AudioSegment
from pydub.playback import play

# Initialize speech recognizer
recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        print("Listening for a song name...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None
    except sr.RequestError:
        print("Speech service unavailable.")
        return None

import yt_dlp
import webbrowser

def play_song_from_youtube(song_name):
    """Search and play the first YouTube result."""
    search_query = f"{song_name} song"
    
    # Fetch video URL
    ydl_opts = {"quiet": True, "default_search": "ytsearch1", "noplaylist": True}
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download=False)
        if "entries" in info and info["entries"]:
            video_url = info["entries"][0]["url"]
            print(f"Playing: {video_url}")
            webbrowser.open(video_url)
        else:
            print("No results found on YouTube.")

def main():
    while True:
        command = listen_command()
        if command:
            if "play" in command:
                song_name = command.replace("play", "").strip()
                print(f"Searching for: {song_name}")
                play_song_from_youtube(song_name)  # Default: Play on YouTube
                # Uncomment below line if you prefer local playback:
                # play_local_music(song_name)

        elif command == "exit":
            print("Exiting assistant...")
            break

if __name__ == "__main__":
    main()
