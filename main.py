from mylib.calculator import add


def add_cli(a, b):
    add(a, b)


# my program
from flask import Flask, request, render_template
import datetime
from dateutil.relativedelta import relativedelta

# import requests
from twilio.rest import Client
from twilioInfo import (
    accountSid,
    authToken,
    myTwilioNumber,
    myPhoneNumber,
    messagingServiceSid,
)

client = Client(accountSid, authToken)


def callTwilio(message):
    client.messages.create(
        messaging_service_sid=messagingServiceSid,
        to=myPhoneNumber,
        from_=myTwilioNumber,
        body=message,
    )


class subscription:
    def __init__(
        self,
        item,
        orderDate,
        paymentMethod,
        paymentAmount,
        state,
        nextPaymentDate,
    ) -> None:
        self.item = item
        self.orderDate = orderDate
        self.paymentMethod = paymentMethod
        self.paymentAmount = paymentAmount
        self.state = state
        self.nextPaymentDate = nextPaymentDate

    def todayIsDue(self, tomoorrow):
        return self.nextPaymentDate == tomoorrow


SubscriptionDB = []

app = Flask(__name__)


@app.route("/add", methods=["GET", "POST"])
def new():
    # to = request.form.get('to')

    if request.method == "POST":
        item = request.form.get("item")

        for i in SubscriptionDB:
            if i.item == item:
                message = f"You already have a {item} subscription."
                return render_template("add.html", message=message)

        orderDate = request.form.get("date")  # need to change to date format
        orderDate = datetime.datetime.strptime(orderDate, "%Y-%m-%d").date()
        paymentMethod = request.form.get("paymentMethod")
        paymentAmount = request.form.get("paymentAmount")

        state = "Active"
        nextPaymentDate = orderDate + relativedelta(months=1)

        newSubscription = subscription(
            item, orderDate, paymentMethod, paymentAmount, state, nextPaymentDate
        )
        SubscriptionDB.append(newSubscription)

        message = f"You add a new subscription {item} on {orderDate}, you paid {paymentAmount} \
                    by {paymentMethod} and your next payment date is {nextPaymentDate}."

        print(SubscriptionDB)

        # twilio api to inform user of new subscription
        # callTwilio(message)

    else:
        message = "Please enter the item and date."
    print(message)
    return render_template("add.html", message=message)


@app.route("/inactivate", methods=["GET", "POST"])
def inactivate():
    if request.method == "POST":
        item = request.form.get("item")

        for s in SubscriptionDB:
            if s.item == item:
                s.state = "Inactive"
                s.nextPaymentDate = None
                message = f"You have successfully inactivate your {item} subscription. You save money!"
            else:
                message = f"You do not have a {item} subscription."

        # twilio api to inform user of new subscription
        # callTwilio(message)
    else:
        message = "Please enter the subscription that you want to inactivate."

    return render_template("delete.html", message=message)


@app.route("/check", methods=["GET"])
def check():
    today = datetime.date.today()
    for s in SubscriptionDB:
        messageToSent = ""
        if s.state == "Active" and s.todayIsDue(today + datetime.timedelta(days=1)):
            message = f"Your {s.item} subscription is due tomorrow. Please make a decision to renew or cancel.\n"
            messageToSent += message
            return

        if s.state == "Active" and s.todayIsDue(today):
            message = f"Your {s.item} subscription is due today. Please make a decision to renew or cancel.\n"
            messageToSent += message
            return

        if s.state == "Active" and s.todayIsDue(today - datetime.timedelta(days=1)):
            s.nextPaymentDate = s.nextPaymentDate + relativedelta(months=1)
            message = f"Your {s.item} subscription is due yesterday. If you did not cancel it, you might be \
            already charged for {s.paymentAmount} in {s.paymentMethod}. The next billing date is \
            {s.nextPaymentDate}. If you already canceled it, please use the inactivate api to help us update.\n"

            messageToSent += message
            return

        # if messageToSent != "":
        #     callTwilio(messageToSent)

        return "No subscription is due today."


@app.route("/")
def home():
    #     # return render_template(('hello.html', name = name))
    return "Welcome to the Subscription Manager!"


# from apscheduler.schedulers.blocking import BlockingScheduler

# def CallApiToCheck():
#     response = requests.get("/check", timeout=5)
#     if response.status_code == 200:
#         print("API called successfully")
#     else:
#         print("API call failed with status code:", response.status_code)


# scheduler = BlockingScheduler()
# scheduler.add_job(CallApiToCheck, "cron", hour=0)
# scheduler.start()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
