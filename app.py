import pathlib
import textwrap
from os import environ
from sys import argv, exit
from rich.progress import track
from rich.console import Console
from rich.markdown import Markdown
from functools import cache
import click
import logging

import google.generativeai as genai
from google.generativeai.types import generation_types
from google.generativeai import *


def mark_print(text_stream: generation_types.GenerateContentResponse):
    console = Console()
    with console.status("[bold green] ...") as status:
        codeStartQuotePresent = False  # flag to track if code block is started
        final_text = ''
        for chunk in text_stream:
            text = chunk.text
            text = text.replace("•", "  *")

            final_text += text

            if '```' in text:
                codeStartQuotePresent = not codeStartQuotePresent

            if codeStartQuotePresent:
                # if the code block is started, wait till we get code block end to print the markdown
                continue

            markdown = Markdown(final_text)
            console.print(markdown)
            final_text = ''


def confiure_genai():
    api_key = environ.get("GEMINI_API_KEY")
    if not api_key:
        logging.error(
            "Missing GEMINI_API_KEY environment variable. Please set it.")
        exit(1)
    try:
        genai.configure(api_key=api_key)
    except Exception as e:  # This catches all exceptions
        logging.error(f"Error configuring Gemini: {e}")
        exit(1)


@cache
def get_model(model_name: str) -> GenerativeModel:
    confiure_genai()
    try:
        return GenerativeModel(model_name)
    except Exception as e:  # This catches all exceptions
        logging.error(f"Error getting model: {e}")
        exit(1)


@cache
def get_chat(model: GenerativeModel) -> ChatSession:
    try:
        return model.start_chat(history=[])
    except Exception as e:  # This catches all exceptions
        logging.error(f"Error starting chat with Gemini: {e}")
        exit(1)


@click.group(help="Command-line interface for interacting with Google's Gemini generative AI models.")
def cli():
    pass


@cli.command()
def models():
    """Display available Gemini models and their capabilities."""
    confiure_genai()
    for model in genai.list_models():
        print(model.name)


@click.option("--model", "-m", type=str, default="gemini-pro",
              help="Name of the Gemini model to use. (default: gemini-pro)")
@cli.command()
def chat(model: str):
    """Start a chat session with the specified Gemini model.

    Type 'quit' or 'exit' to end the conversation.
    """
    model_obj = get_model(model)
    print(f"Welcome! You are chatting with the {model_obj.model_name} model.")
    print(f"Type 'quit' or 'exit' to end the conversation.")

    while True:
        print("> ", end="")
        inp = input()
        if not inp:
            continue
        if inp.lower().strip() in ("quit", "exit"):
            return

        resp = get_chat(model_obj).send_message(inp, stream=True)
        mark_print(resp)


@cli.command(name="tell")
@click.argument("prompt", nargs=-1)
@click.option("--model", "-m", type=str, default="gemini-pro",
              help="Name of the Gemini model to use. (default: gemini-pro)")
def query(model, prompt):
    """Generate content using the specified Gemini model and prompt."""
    model_obj = get_model(model)
    prompt = " ".join(list(prompt))
    resp = model_obj.generate_content(prompt, stream=True)
    mark_print(resp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        cli()
    except Exception as e:  # This catches all exceptions
        logging.error(f"Error during chat: {e}")
        exit(1)
