#!/usr/bin/env python3
import pathlib
import textwrap
from os import environ
from sys import argv
from rich.console import Console
from rich.markdown import Markdown

import google.generativeai as genai


def mark_print(text):
    console = Console()
    markdown = Markdown(text)
    console.print(markdown)


# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def get_model():
    api_key = environ['GEMINI_API_KEY']
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro')


if __name__ == '__main__':
    model = get_model()
    prompt = ' '.join(argv[1:])
    print(prompt)
    resp = model.generate_content(prompt)
    mark_print(resp.text)



