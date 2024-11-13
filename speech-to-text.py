#!/bin/env python3
import openai
import os
import sys

HELP_MESSAGE = """This is a simple tools that extracts the text from an audio file using the openai api.
Usage: OPENAI_API_KEY='' {} <path_to_audio_file>
"""


def main():
    if sys.argv[1] in ["-h", "--help"]:
        print(HELP_MESSAGE.format(sys.argv[0]))
        return 0

    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not os.getenv("OPENAI_API_KEY"):
        print("please provide OPENAI_API_KEY environment variable")
        return 1

    client = openai.OpenAI()

    audio_file_path = sys.argv[1] if len(sys.argv) > 1 else None
    if not audio_file_path or not os.path.isfile(audio_file_path):
        print("please provide a valid path to an audio file")
        return 1
    audio_file = open(audio_file_path, 'rb')
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language="en",
        response_format="text"
    )
    print(transcription)

    return 0


if __name__ == "__main__":
    main()
