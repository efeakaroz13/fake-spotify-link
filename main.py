from flask import Flask, render_template, request, redirect
#import pyrebase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import base64

def notify(reciever, message, title):
        server = smtplib.SMTP("smtp-mail.outlook.com", 587) 
        server.ehlo()
        server.starttls()
        gmail_sender = "efeakaroz@outlook.com"
        gmail_passwd = "efeZeynep123"

        message = "Subject: {}\n\n{}".format(title, message)
        server.login(gmail_sender, gmail_passwd)

        server.sendmail(gmail_sender, "efeakaroz13@gmail.com", message.encode("utf-8"))

class Openspotify:
    app = Flask(__name__)

    

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/create_session")
    def create_session():
        email = request.args.get("email")
        realspotifylink = request.args.get("URL")
        notify(
            email,
            "We created your fake link we will email all views which comes to your profile!\n\n"
            + str({"email": email, "reallink": realspotifylink}),
            "Kentel fake link service",
        )
        return {"done": True}


if __name__ == "__main__":
    Openspotify.app.run(debug=True)
