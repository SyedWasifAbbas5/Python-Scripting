#!/usr/bin/python

import psutil
import smtplib
import time
from email.mime.text import MIMEText

def send_email(subject, message, to_email):
    from_email = "your_email@example.com"  # Update with your email address
    password = "your_password"  # Update with your email password

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    server = smtplib.SMTP('smtp.example.com', 587)  # Update with your SMTP server details
    server.starttls()
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()

def monitor_cpu(interval=1, threshold=90, email=None):
    while True:
        cpu_percent = psutil.cpu_percent(interval=interval)
        print(f"CPU Usage: {cpu_percent}%")

        if email and cpu_percent > threshold:
            subject = "High CPU Usage Alert"
            message = f"CPU Usage is at {cpu_percent}%"
            send_email(subject, message, email)

        time.sleep(interval)

if __name__ == "__main__":
    email = "recipient@example.com"  # Update with the recipient's email address
    monitor_cpu(email=email)