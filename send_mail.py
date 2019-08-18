import smtplib
from email.mime.text import MIMEText # HTML mail text manipulation

def send_mail(customer, dealer, rating, comments):
    # Service setup
    port = 2525 # Mailtrap config
    smtp_server = "smtp.mailtrap.io"
    login = "d3c3f77e236b24" # Your Mailtrap access data
    password = "b39945aa84bc33"
    message = f"<h3>Tu evaluación</h3><ul><li>Customer: {customer}</li><li>Delaer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>" # Body mail message using format
    sender_email = "email1@example.com"
    receiver_email = "email2@example.com"
    msg = MIMEText(message, 'html')
    msg['Subject'] = "Evaluación Lexus"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
