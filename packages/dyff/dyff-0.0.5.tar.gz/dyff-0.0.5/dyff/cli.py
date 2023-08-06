"""Command line utility for uploading file contents to Google bucket.
Providing you already have a user account, the CLI will take your
user account identifier, password, and path and then wrap up the path
and send it to the Google Bucket.
"""

import http.client
import json

import click


def login(username, password):
    """Login to the dyff servers"""
    print(
        "In the future this will actually produce credentials to be posted to the server"
    )
    return "done"


def upload_files():
    """todo"""
    connection = http.client.HTTPConnection("localhost:8080")
    connection.request("GET", "/")
    response = connection.getresponse()
    print("Status: {} and reason: {}".format(response.status, response.reason))
    print(json.loads(response.read())["url"])
    connection.close()


@click.group()
@click.version_option()
def cli_main():
    pass


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.argument("username")
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=False)
def upload(path, username, password):
    click.echo("upload: %s" % path)
    click.echo("username: %s" % username)
    click.echo("password: %s" % password)
    upload_files()


cli_main.add_command(upload)

if __name__ == "__main__":
    cli_main()
