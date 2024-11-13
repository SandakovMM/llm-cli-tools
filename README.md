# LLM CLI Tools

This project aggregates various LLM-based tools for the command line, designed for personal tasks. Currently, it is based on OpenAI's GPT.

## Tools Included

- **gpt.py**: A script to interact with OpenAI GPT for generating text based on prompts.
- **rewrite-please.py**: A tool to rewrite text using GPT.
- **speech-to-text.py**: A script to convert speech to text using GPT.

## Usage

Each script can be run from the command line. Ensure you have the necessary dependencies installed and the appropriate API keys configured.
API keys could be passed by OPENAI_API_KEY environment variable. For example:
```
OPENAI_API_KEY="sk-foobar" ./rewrite-please.py "message in slack"
```

## Installation
1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.