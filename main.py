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


from flask import Flask, request, render_template
from twilio.rest import Client
from twilioInfo import (
    accountSid,
    authToken,
    myTwilioNumber,
    myPhoneNumber,
    messagingServiceSid,
)

app = Flask(__name__)

client = Client(accountSid, authToken)


@app.route("/add-a-subscription", methods=["GET", "POST"])
def new():
    # to = request.form.get('to')

    if request.method == "POST":
        item = request.form.get("item")
        date = request.form.get("date")
        message = "You start a subscription " + item + " on " + date + "."
        client.messages.create(
            messaging_service_sid=messagingServiceSid,
            to=myPhoneNumber,
            from_=myTwilioNumber,
            body=message,
        )
    else:
        message = "Please enter the item and date."

    return render_template("subscription.html", message=message)


@app.route("/")
def home():
    #     # return render_template(('hello.html', name = name))
    return "Welcome to the Subscription Manager!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
