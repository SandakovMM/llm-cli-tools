#!/bin/env python3
from openai import OpenAI
import os
from optparse import OptionParser
import sys

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

HELP_MESSAGE = """This tool helps to make summery from chats to save you time of reading.
Use OPENAI_API_KEY environment variable to pass your openai api key.

Please be careful with sensitive data, as it will be passed to openai servers.

The sentence should be passed through stdin. Example:
Anna, [10:00 AM] : Hello, how are you?
Bob, [10:01 AM] : Hi, I am fine, how are you?

usage: OPENAI_API_KEY='' %prog [options]
"""


def main():

    opts = OptionParser(usage=HELP_MESSAGE)
    opts.add_option("-m", "--model", dest="model", type="string", default="gpt-4o",
                    help="gpt model to use")
    opts.add_option("-l", "--language", dest="language", type="string", default="en",
                    help="language of the chat and response")

    (options, _) = opts.parse_args()

    TASK_PROMPT = "Could you please do chat summery with main discussed themes. Each theme should be split in different paragraph. Please make it as compact as possible, but keep all the facts."
    if options.language != "en":
        TASK_PROMPT += "Please use {} language for the response.".format(options.language)

    sentence = ""
    for line in sys.stdin:
        sentence += line + "\n"

    if not os.getenv("OPENAI_API_KEY"):
        print("please provide OPENAI_API_KEY environment variable")
        return 1

    request = [
        {"role": "system", "content": TASK_PROMPT.format()},
        {"role": "user", "content": sentence},
    ]
    print("GPT answer:")

    openai_call = client.chat.completions.create(model=options.model, messages=request)

    print(openai_call.choices[0].message.content)
    return 0


if __name__ == "__main__":
    main()
