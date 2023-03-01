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

# ,  request
from twilio.rest import Client
from twilioInfo import accountSid, authToken, myTwilioNumber, myPhoneNumber

app = Flask(__name__)

client = Client(accountSid, authToken)


@app.route("/send-sms/<message>", methods=["GET"])
def send_sms(message):
    # to = request.form.get('to')
    # message = request.form.get('message')
    messageContent = message
    client.messages.create(to=myPhoneNumber, from_=myTwilioNumber, body=messageContent)

    return "Message sent!"


@app.route("/")
def home():
    #     # return render_template(('hello.html', name = name))
    return "Welcome to the Subscription Manager!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
