import smtplib

sender_email = "sender@example.com"
receiver_emails = ["receiver1@example.com", "receiver2@example.com"]
password = "password"
message = "Subject: Test email from Python\n\nThis is a test email sent from Python."

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)

for receiver_email in receiver_emails:
    server.sendmail(sender_email, receiver_email, message)

server.quit()
