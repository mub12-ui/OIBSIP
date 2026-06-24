import smtplib
from email.message import EmailMessage
from config.secrets import EMAIL_ADDRESS, EMAIL_PASSWORD


def send_email(receiver_email, subject, body):
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = receiver_email
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return "Email sent successfully."

    except Exception as e:
        return f"Failed to send email: {e}"