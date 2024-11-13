#!/bin/env python3
from openai import OpenAI
import os
from optparse import OptionParser
import sys

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TASK_PROMPT = "Could you please rewrite following {} in perfect simple english. {}"

HELP_MESSAGE = """This tool helps to rewrite sentences for clearer communication.
It substitutes sensitive information before sending the sentence to the GPT servers.
Use OPENAI_API_KEY environment variable to pass your openai api key.

The sentence should be passed through stdin.

usage: OPENAI_API_KEY='' %prog [options]
"""


def main():

    opts = OptionParser(usage=HELP_MESSAGE)
    opts.add_option("-t", "--type", dest="type", type="string", default="sentence",
                    help="type of you sentence, for example 'git commit message'")
    opts.add_option("-p", "--prompt", dest="prompt", type="string", default="",
                    help="prompt injection if you want to make result more formal for example")
    opts.add_option("-m", "--model", dest="model", type="string", default="gpt-4o",
                    help="gpt model to use")

    (options, _) = opts.parse_args()

    sentence = ""
    for line in sys.stdin:
        sentence += line + "\n"

    if not os.getenv("OPENAI_API_KEY"):
        print("please provide OPENAI_API_KEY environment variable")
        return 1

    request = [
        {"role": "system", "content": TASK_PROMPT.format(options.type, options.prompt)},
        {"role": "user", "content": sentence},
    ]
    print("GPT answer:")

    openai_call = client.chat.completions.create(model=options.model, messages=request)

    print(openai_call.choices[0].message.content)
    return 0


if __name__ == "__main__":
    main()
