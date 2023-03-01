"""
Main cli or app entry point
"""

from mylib.calculator import add
import click


@click.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a, b):
    click.echo(add(a, b))


# test
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    #     # return render_template(('hello.html', name = name))
    return "Welcome to the Subscription Manager!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
