import smtplib, ssl
import os
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()
# st.write(st.session_state)
USERNAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = USERNAME
    password = PASSWORD

    receiver = "testmanishrai@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)