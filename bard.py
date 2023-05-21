"""
Usage:
    bard.py [--debug] [--interactive]
    bard.py [--debug] [INPUT...]
    bard.py (-h | --help)

Options:
    -h --help        Show this screen
    --interactive    Interactive chat mode
    --debug          Enable debugging output

"""


from bardapi import Bard
from os import environ
from rich.console import Console
from rich.markdown import Markdown
from docopt import docopt


debug_enabled = False

def run_interactive(bard) :
    try :
        while True:
            user_input = input("\U0001F464 >> ")
            if user_input == 'exit' :
                return

            print()
            print_markdown_answer(bard, user_input)
            print('-'*100, "\n")

    except KeyboardInterrupt :
        return


def get_answer(bard, user_input) :
    response = bard.get_answer(args)
    print_if_debug_enabled("response", response)
    return response


def print_markdown_answer(bard, user_input) :
    response = bard.get_answer(user_input)
    print_if_debug_enabled("response", response)
    console = Console()
    md = Markdown("\U0001F916 " + response['content'])
    console.print(md)


def print_if_debug_enabled(name, text):
    if debug_enabled == False :
        return

    print(name + " :" , text)


if __name__ == "__main__" :
    arguments = docopt(__doc__)
    print_if_debug_enabled("arguments", arguments)

    interactive_enabled = arguments['--interactive']
    debug_enabled = arguments['--debug']
    user_input = " ".join(arguments['INPUT'])



    token = environ.get('BARD_TOKEN')
    if not token or token.strip() == "" :
        print("api token not found")
    bard = Bard(token = token)


    if interactive_enabled or user_input.strip() == "" :
        run_interactive(bard)
    else :
        print_markdown_answer(bard, user_input)

