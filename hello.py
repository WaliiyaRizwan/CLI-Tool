#!/usr/bin/env python

# Import the click library, which is used for creating CLI interfaces
import click

# Import the glob library, which is used for searching files
import glob

# Define a CLI command called "search" with "path" and "ftype" options
@click.command()
@click.option(
    "--path",
    prompt="Path to search for csv files",
    help="This is the path to search for files: /tmp",
)
@click.option(
    "--ftype", prompt="Pass in the type of file", help="Pass in the file type:  i.e csv"
)
def search(path, ftype):
    # Use the glob library to search for files that match a pattern like "*.csv" in the specified path
    results = glob.glob(f"{path}/*.{ftype}")
    # Use click to print a message indicating that matches have been found
    click.echo(click.style("Found Matches:", fg="red"))
    # Loop through the list of matching files and use click to print each one
    for result in results:
        click.echo(click.style(f"{result}", bg="blue", fg="white"))


if __name__ == "__main__":
    # Disable a warning from pylint
    # pylint: disable=no-value-for-parameter
    # Call the "search" command if this script is being run directly
    search()

# Explanation:
# - The shebang line at the top of the file specifies the path to the Python interpreter that should be used to run this script.
# - The click and glob libraries are imported.
# - The "search" command is defined with "path" and "ftype" options, using click.
# - The "search" command uses glob to search for files that match a pattern like "*.csv" in the specified path.
# - The "search" command uses click to print a message indicating that matches have been found, and to print each matching file.
# - The "if __name__ == '__main__':" block ensures that the "search" command is only called if this script is being run directly.
# - The "pylint: disable=no-value-for-parameter" comment is used to disable a warning from pylint.

