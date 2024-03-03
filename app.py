#!/usr/bin/env python3
import pathlib
import textwrap
from os import environ
from sys import argv
from rich.console import Console
from rich.markdown import Markdown
from functools import cache
import click

import google.generativeai as genai


def mark_print(text_stream):
    console = Console()
    for chunk in text_stream:
        text = chunk.text
        text = text.replace('•', '  *')
        markdown = Markdown(text)
        console.print(markdown)


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


@cache
def get_model():
    api_key = environ['GEMINI_API_KEY']
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro')


@cache
def get_chat():
    model = get_model()
    return model.start_chat(history=[])


@click.group()
def cli():
    pass


@cli.command
def chat():
    while True:
        print("> ", end='')
        inp = input()
        if inp.strip() == '':
            continue
        if inp.strip() == 'quit' or inp.strip() == 'exit':
            return
        resp = get_chat().send_message(inp, stream=True)
        mark_print(resp)


@cli.command(name='tell')
@click.argument('prompt', nargs=-1)
def query(prompt):
    prompt = ' '.join(list(prompt))
    resp = get_model().generate_content(prompt, stream=True)
    mark_print(resp)


if __name__ == '__main__':
    cli()
