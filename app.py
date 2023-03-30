#!/usr/bin/env python

# Import the click library, which is used for creating CLI interfaces
import click

# Define a CLI command called "hello" with an optional "name" argument
@click.command()
@click.option("--name")
def hello(name):
    # Use the click library to print a message that includes the value of the "name" argument
    click.echo(f'Hello {name}!')

# Check if this script is being run directly, and if so, call the "hello" command
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()

# Explanation:

# - When the "hello" command is run, it uses click to print a message that includes the value of the "name" argument.
# - The "if __name__ == '__main__':" block ensures that the "hello" command is only called if this script is being run directly.
