#!/bin/env python3
from openai import OpenAI
import os
from optparse import OptionParser

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

HELP_MESSAGE = """usage: OPENAI_API_KEY='' %prog [options]

Just send a request to gpt through the openai api.
The script will read from stdin and send the request to openai. It waits until EOF or second empty line to start the request.
To exit the script type 'exit' or 'quit' and press enter twice.
"""

exit_santances = [
    "",
    "\n",
    "exit",
    "quit",
    "bye",
    "goodbye",
    "\\q",
    "\\quit",
    "\\exit",
]


def main():

    opts = OptionParser(usage=HELP_MESSAGE)
    opts.add_option("-t", "--type", dest="type", type="string", default="sentence",
                    help="type of you sentence, for example 'git commit message'")
    opts.add_option("-m", "--model", dest="model", type="string", default="gpt-4o",
                    help="gpt model to use")

    (options, _) = opts.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        print("please provide OPENAI_API_KEY environment variable")
        return 1

    intro_message = "Hello. I'm GPT cli tool. How can I help you?"
    print(intro_message)
    request = [
        {"role": "system", "content": intro_message}
    ]

    while True:
        sentence = ""
        while True:
            try:
                line = input("> ")
                if line == "":
                    break
                sentence += line
            except EOFError:
                break

        if sentence in exit_santances:
            break

        request.append({"role": "user", "content": sentence})
        print("GPT answering...", end="\r")

        openai_call = client.chat.completions.create(model=options.model, messages=request)

        responce = openai_call.choices[0].message.content

        print(responce)
        request.append({"role": "system", "content": responce})

    return 0


if __name__ == "__main__":
    main()
